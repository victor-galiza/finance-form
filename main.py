from flask import Flask, render_template
from flask import redirect, url_for


app = Flask(__name__)

@app.route("/registrar")
def register():
    return render_template("register.html")

@app.route("/entrar")
def login():
    return render_template("login.html")

@app.route("/termos-e-condicoes")
def terms():
    return render_template("terms.html")

@app.route("/recuperar-senha")
def forgotPassword():
    return render_template("forgot-password.html")

@app.route("/alterar-senha")
def changePassword():
    return render_template("change-password.html")

@app.route("/senha-alterada-com-sucesso")
def successfulChange():
    return render_template("successful-change.html")



@app.route('/')
def index():
    return redirect(url_for('login'))  # ou outra página

# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)
