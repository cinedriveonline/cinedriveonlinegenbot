from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/resultado', methods=['POST'])
def procesar():
    nombre = request.form.get("nombre")
    idioma = request.form.get("idioma")
    genero = request.form.get("genero")
    link = request.form.get("link")
    permisos = request.form.get("permisos")
    love = request.form.get("love")
    return render_template("resultado.html", nombre=nombre, idioma=idioma, genero=genero, link=link, permisos=permisos, love=love)

if __name__ == '__main__':
    app.run(debug=True)