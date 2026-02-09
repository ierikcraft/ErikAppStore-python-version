# APP WEB

# RED HTTP, HTTPS

# HTTPs IPv6 127,502 MAC

# REST FULL API

# ENCABEZADOS, CODIGOS 404, 500, 200, metadata

from flask import Flask

app = Flask(__name__)

# Endpoint()

# https://120.0120.1.200/

@app.route('/')
def home():
    return """
    <h1>Hola Mundo desde Flask</h1>
    <p>Esta es mi primera app web con Flask</p>
    <a href="/proyecto">Ir a proyectos</a>
    
    
"""


@app.route('/proyecto')
def proyecto():

    lista = ["CALCULADORA", "ATM", "JUEGO CON PYGAME"]

    return f"""
    <h1>Proyectos</h1>
    <ul>
        <li>
        {lista[0]}
        </li>
        <li>
        {lista[1]}
        </li>
        <li>
        {lista[2]}
        </li>
    </ul>

    
    
"""
# ENDPOINT PARA OTRA VENTANA




# esto debe ser el final del archivo

if __name__ == '__main__':
    app.run(debug=True)
