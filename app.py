"""
DevSecOps Lab - Aplicação Vulnerável para Fins Educacionais
ATENÇÃO: Esta aplicação contém vulnerabilidades INTENCIONAIS para demonstração.
NÃO USE EM PRODUÇÃO!
"""

import os
import sqlite3
import subprocess
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = os.getenv('DATABASE_PATH', 'users.db')

def get_db():
    """Conecta ao banco de dados SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados com dados de exemplo"""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Dados de exemplo
    conn.execute("INSERT OR IGNORE INTO users (id, username, email, password) VALUES (1, 'admin', 'admin@example.com', 'admin123')")
    conn.execute("INSERT OR IGNORE INTO users (id, username, email, password) VALUES (2, 'user', 'user@example.com', 'user123')")
    conn.commit()
    conn.close()

# ============================================
# ENDPOINTS DA APLICAÇÃO
# ============================================

@app.route('/')
def home():
    """Página inicial"""
    return jsonify({
        'app': 'DevSecOps Lab',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': [
            'GET /health',
            'GET /users',
            'GET /user?id=1',
            'GET /search?q=termo',
            'POST /login'
        ]
    })

@app.route('/health')
def health():
    """Health check para o container"""
    return jsonify({'status': 'healthy'})

@app.route('/users')
def list_users():
    """Lista todos os usuários"""
    conn = get_db()
    users = conn.execute('SELECT id, username, email FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

# ============================================
# VULNERABILIDADES INTENCIONAIS (PARA DEMO)
# ============================================

@app.route('/user')
def get_user():
    """
    VULNERABILIDADE: SQL Injection
    Exemplo de exploração: /user?id=1 OR 1=1
    """
    user_id = request.args.get('id', '1')
    conn = get_db()
    # INSEGURO: Concatenação direta de input do usuário
    query = f"SELECT * FROM users WHERE id = {user_id}"
    try:
        user = conn.execute(query).fetchone()
        conn.close()
        if user:
            return jsonify(dict(user))
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search')
def search():
    """
    VULNERABILIDADE: Cross-Site Scripting (XSS)
    Exemplo de exploração: /search?q=<script>alert('XSS')</script>
    """
    query = request.args.get('q', '')
    # INSEGURO: Renderiza input do usuário sem sanitização
    html = f"""
    <html>
        <head><title>Search Results</title></head>
        <body>
            <h1>Resultados para: {query}</h1>
            <p>Nenhum resultado encontrado.</p>
        </body>
    </html>
    """
    return render_template_string(html)

@app.route('/ping')
def ping():
    """
    VULNERABILIDADE: Command Injection
    Exemplo de exploração: /ping?host=localhost;cat /etc/passwd
    """
    host = request.args.get('host', 'localhost')
    # INSEGURO: Input do usuário passado direto para shell
    try:
        result = subprocess.check_output(f'ping -c 1 {host}', shell=True, text=True)
        return f"<pre>{result}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>Error: {e}</pre>", 500

@app.route('/login', methods=['POST'])
def login():
    """
    VULNERABILIDADE: Credenciais em log
    """
    data = request.get_json() or {}
    username = data.get('username', '')
    password = data.get('password', '')
    
    # INSEGURO: Loga credenciais (expostas em logs do container)
    print(f"Login attempt: username={username}, password={password}")
    
    conn = get_db()
    # INSEGURO: SQL Injection no login
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    user = conn.execute(query).fetchone()
    conn.close()
    
    if user:
        return jsonify({'message': 'Login successful', 'user': dict(user)})
    return jsonify({'error': 'Invalid credentials'}), 401

# ============================================
# INICIALIZAÇÃO
# ============================================

if __name__ == '__main__':
    init_db()
    # INSEGURO: Debug mode em produção
    app.run(host='0.0.0.0', port=5000, debug=True)
