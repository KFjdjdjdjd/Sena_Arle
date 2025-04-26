from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

conexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='bd_restaurante')
cur = conexion.cursor()

app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template('pagina1.html')


# Mostrar la informacion de la base de datos
@app.route('/pagina2', methods=["GET", "POST"])
def pagina2():
    conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
    cur = conexion.cursor()
    
    sql = "SELECT * FROM platos"
    cur.execute(sql)
    
    return render_template('pagina2.html', platos = cur)


# Agregar nueva informacion a la base de datos
@app.route('/agregar_plato', methods=["GET", "POST"])
def pagina2_agregar_plato():
    if request.method=='POST':
        id_plato=request.form["id_plato"]
        nombre_plato=request.form["nombre_plato"]
        id_tipo_plato=request.form["id_tipo_plato"]
        precio=request.form["precio"]
        
        conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
        cur = conexion.cursor()
        
        sql = "INSERT INTO platos (id_plato, nombre_plato, id_tipo_plato, precio) VALUES (%s, %s, %s, %s)"
        val = (id_plato, nombre_plato, id_tipo_plato, precio)
        
        cur.execute(sql, val)
        conexion.commit()
        
    return redirect(url_for('pagina2'))


# Parte del Crud(Borrar)
@app.route("/borrarplato/<string:id>")
def borrar_plato(id):
    conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
    cur = conexion.cursor()
    
    sql = "DELETE FROM platos WHERE id_plato= {0}".format(id)
    cur.execute(sql)
    conexion.commit()
    
    return redirect(url_for("pagina2"))

@app.route("/editarplato/<string:id>")
def editar_plato(id):
    conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
    cur = conexion.cursor()
    
    sql = "SELECT * FROM platos WHERE id_plato= {0}".format(id)
    cur.execute(sql)
    data = cur.fetchall()
    
    return render_template("editar_plato.html", cat = data[0])

@app.route("/actualizarcliente/<string:id>", methods=["POST"])
def actualizar_cliente(id):
    if request.method=="POST":
        conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
        cur = conexion.cursor()
            
        nombre_plato=request.form["nombre_plato"]
        id_tipo_plato=request.form["id_tipo_plato"]
        precio=request.form["precio"]
        id_plato=request.form["id_plato"]
        
        sql = "UPDATE platos SET nombre_plato = %s, id_tipo_plato = %s, precio = %s WHERE id_plato = %s"
        val = (nombre_plato, id_tipo_plato, precio, id_plato)
        cur.execute(sql, val)
        conexion.commit()
        
        return redirect(url_for("pagina2"))

@app.route('/pagina3', methods=["GET", "POST"])
def pagina3():
    conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
    cur = conexion.cursor()
    
    sql = "SELECT * FROM pedidos"
    cur.execute(sql)
    
    return render_template('pagina3.html', pedidos = cur)

@app.route('/agregar_pedido', methods=["GET", "POST"])
def pagina3_agregar_pedido():
    if request.method=="POST":
        id_pedido=request.form["id_pedido"]
        fecha_pedido=request.form["fecha_pedido"]
        id_cliente=request.form["id_cliente"]
        total_price=request.form["total_price"]
        
        conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
        cur = conexion.cursor()
        
        sql = "INSERT INTO pedidos (id_pedido, fecha_pedido, id_cliente, total_price) VALUES (%s, %s, %s, %s)"
        val = (id_pedido, fecha_pedido, id_cliente, total_price)

        cur.execute(sql, val)
        conexion.commit()
        
    return redirect(url_for("pagina3"))

@app.route("/borrarpedido/<string:id>")
def borrar_pedido(id):
    conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
    cur = conexion.cursor()
    
    sql = "DELETE FROM pedidos WHERE id_pedido= {0}".format(id)
    cur.execute(sql)
    conexion.commit()
    
    return redirect(url_for("pagina3"))

@app.route("/editarpedido/<string:id>")
def editar_pedido(id):
    conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
    cur = conexion.cursor()
    
    sql = "SELECT * FROM pedidos WHERE id_pedido= {0}".format(id)
    cur.execute(sql)
    data = cur.fetchall()
    
    return render_template("editar_pedido.html", cat = data[0])

@app.route("/actualizarpedido/<string:id>", methods=["POST"])
def actualizar_pedido(id):
    if request.method=="POST":
        conexion = mysql.connector.connect (host="localhost", user="root", passwd="", db="bd_restaurante")
        cur = conexion.cursor()
        
        fecha_pedido=request.form["fecha_pedido"]
        id_cliente=request.form["id_cliente"]
        total_price=request.form["total_price"]
        id_pedido=request.form["id_pedido"]
        
        sql = "UPDATE pedidos SET fecha_pedido = %s, id_cliente = %s, total_price = %s WHERE id_pedido = %s"
        val = (fecha_pedido, id_cliente, total_price, id_pedido)
        cur.execute(sql, val)
        conexion.commit()
        
        return redirect(url_for("pagina3"))
        
@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html')

if __name__ == '__main__':
    app.run(port=3332, debug=True)