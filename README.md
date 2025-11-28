# Aula 04 - Segurança de Containers

## 🎯 Objetivo

Implementar hardening de containers, scan de imagens e segurança de IaC.

## 📹 Vídeos desta Aula

| Vídeo | Tema | O que você vai fazer |
|-------|------|---------------------|
| 01 | Hardening Dockerfile | Aplicar boas práticas de segurança |
| 02 | Scan de Imagens | Trivy para scan e ECR scan |
| 03 | IaC Security | Checkov para Terraform |

## 📁 Estrutura do Repositório

```
.
├── app.py
├── requirements.txt
├── Dockerfile            # Versão insegura (para comparar)
├── Dockerfile.secure     # Versão segura
├── .dockerignore
├── .hadolint.yaml        # Config do linter Dockerfile
├── .checkov.yaml         # Config do Checkov
├── terraform/            # IaC de exemplo
│   └── main.tf
├── .github/
│   └── workflows/        # (Criado durante a aula)
└── docs/
    ├── HANDS-ON-04-01.md
    ├── HANDS-ON-04-02.md
    ├── HANDS-ON-04-03.md
    └── CHEATSHEET.md
```

## ⚙️ Pré-requisitos

- [ ] Aula 03 concluída
- [ ] ECR configurado

## 📚 Documentação

| Vídeo | Hands-on |
|-------|----------|
| 01 - Hardening Dockerfile | [HANDS-ON-04-01.md](docs/HANDS-ON-04-01.md) |
| 02 - Scan de Imagens | [HANDS-ON-04-02.md](docs/HANDS-ON-04-02.md) |
| 03 - IaC Security | [HANDS-ON-04-03.md](docs/HANDS-ON-04-03.md) |

**Referência rápida**: [Cheatsheet](docs/CHEATSHEET.md)

---

**FIAP - Pós Tech DevSecOps**
