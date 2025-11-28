# Aula 04 - Cheatsheet

## Hadolint

```bash
# Instalar
brew install hadolint  # Mac

# Lint Dockerfile
hadolint Dockerfile

# Ignorar regras
hadolint --ignore DL3008 Dockerfile
```

## Trivy Image Scan

```bash
# Scan imagem local
trivy image app:latest

# Scan com severity
trivy image --severity HIGH,CRITICAL app:latest

# Output JSON
trivy image -f json -o results.json app:latest
```

## ECR Scan

```bash
# Habilitar scan on push
aws ecr put-image-scanning-configuration \
  --repository-name devsecops-app \
  --image-scanning-configuration scanOnPush=true \
  --profile fiapaws

# Ver findings
aws ecr describe-image-scan-findings \
  --repository-name devsecops-app \
  --image-id imageTag=latest \
  --profile fiapaws
```

## Checkov

```bash
# Instalar
pip install checkov

# Scan Terraform
checkov -d terraform/

# Scan Dockerfile
checkov -f Dockerfile

# Ignorar check específico
checkov -d . --skip-check CKV_AWS_18
```

## Dockerfile Best Practices

```dockerfile
# 1. Imagem slim
FROM python:3.11-slim

# 2. Usuário não-root
RUN useradd -r appuser
USER appuser

# 3. Multi-stage
FROM builder AS build
FROM production AS final

# 4. Healthcheck
HEALTHCHECK CMD curl -f http://localhost/ || exit 1

# 5. .dockerignore
# Sempre usar!
```
