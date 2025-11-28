# ============================================
# DOCKERFILE INSEGURO - PARA DEMONSTRAÇÃO
# Este Dockerfile será corrigido na Aula 04
# ============================================

FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# PROBLEMAS DE SEGURANÇA (serão corrigidos na Aula 04):
# 1. Roda como root
# 2. Imagem base grande
# 3. Sem health check
# 4. Debug mode ativo

EXPOSE 5000

CMD ["python", "app.py"]
