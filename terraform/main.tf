# ============================================
# TERRAFORM INSEGURO - PARA DEMONSTRAÇÃO
# Este arquivo será corrigido durante a aula
# ============================================

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# ❌ PROBLEMA 1: S3 Bucket público
resource "aws_s3_bucket" "data" {
  bucket = "devsecops-data-bucket-insecure"
  
  tags = {
    Environment = "dev"
    Project     = "devsecops"
  }
}

# ❌ PROBLEMA 2: ACL pública
resource "aws_s3_bucket_acl" "data" {
  bucket = aws_s3_bucket.data.id
  acl    = "public-read"  # Checkov vai detectar!
}

# ❌ PROBLEMA 3: Sem versionamento
# (Checkov vai alertar sobre isso)

# ❌ PROBLEMA 4: Sem encryption
# (Checkov vai alertar sobre isso)

# ❌ PROBLEMA 5: Sem logging
# (Checkov vai alertar sobre isso)

# Security Group muito permissivo
resource "aws_security_group" "web" {
  name        = "web-insecure"
  description = "Web security group"

  # ❌ PROBLEMA 6: Aberto para o mundo
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Checkov vai detectar!
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
