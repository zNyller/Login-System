from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Mundo!'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        return f'Olá, {name}  {lastname}! Seja bem-vindo!'
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)