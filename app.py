from flask import Flask, render_template, request
class Cancion:
    def __init__(self,titulo,categoria,idioma):
        self.titulo = titulo
        self.categoria = categoria
        self.idioma = idioma
        
cancion1 = Cancion('La guitarra','Pop','Catellano')
cancion2 = Cancion('Para no verte más','Pop','Catellano')
cancion3 = Cancion('Balada para un gordo','Balada','Catellano')
lista = [cancion1,cancion2,cancion3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('listar.html', titulo='Canciones', musicas=lista)

@app.route('/nuevoregistro')
def nuevoregistro():
    return render_template('nuevoRegistro.html',titulo='Nueva Canción')

@app.route('/crear',methods=['POST',])
def crear():
    titulo =request.form['titulo']
    categoria =request.form['categoria']
    idioma =request.form['idioma']
    cancion =Cancion(tittulo,categoria,idioma)
    lista.append(cancion)
    return render_template('listar.html', titulo='Canciones', musicas=lista)

app.run(host="0.0.0.0",port=5000)