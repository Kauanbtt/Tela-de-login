from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Necessário para usar o flash

# Simulação de um usuário existente para autenticação
USUARIO = {
    "email": "usuario@exemplo.com",
    "senha": "senha123"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if email == USUARIO['email'] and senha == USUARIO['senha']:
            flash('Login realizado com sucesso!', 'sucesso')
            return redirect(url_for('home'))
        else:
            flash('Email ou senha incorretos.', 'erro')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
