import sqlite3

# Conectar o crear la base de datos
conn = sqlite3.connect('PCH.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Definir una sentencia SQL para crear una tabla
crear_tabla_sql0 = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    password TEXT NOT NULL,
    tipo TEXT NOT NULL,
    email TEXT NOT NULL
)
'''
cursor.execute(crear_tabla_sql0)

crear_tabla_sql1 = '''
CREATE TABLE IF NOT EXISTS eventos (
    id_evento INTEGER PRIMARY KEY,
    tipo INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    conteo INTEGER NOT NULL,
    estimados_a_ir INTEGER NOT NULL,
    cuantos_fueron INTEGER NOT NULL,
    nombre TEXT NOT NULL 
)
'''
cursor.execute(crear_tabla_sql1)

crear_tabla_sql2 = '''
CREATE TABLE IF NOT EXISTS boleto (
    id_boleto INTEGER PRIMARY KEY,
    tipo_evento INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    lugar TEXT NOT NULL,
    precio TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    existencia TEXT NOT NULL,
    conteo TEXT NOT NULL,
    nombre_evento TEXT NOT NULL 
)
'''
cursor.execute(crear_tabla_sql2)

crear_tabla_sql3 = '''
CREATE TABLE IF NOT EXISTS compras_usuarios (
    id_compra INTEGER PRIMARY KEY,
    id_boleto INTEGER NOT NULL,
    tipo_evento INTEGER NOT NULL,
    usuario TEXT NOT NULL,
    correo TEXT NOT NULL,
    cantidad_boletos INTEGER NOT NULL,
    fecha_compra TEXT NOT NULL,
    fecha_evento TEXT NOT NULL,
    nombre_evento TEXT NOT NULL 
)
'''
cursor.execute(crear_tabla_sql3)

crear_tabla_sql4 = '''
CREATE TABLE IF NOT EXISTS cine (
    id_cine INTEGER PRIMARY KEY,
    tipo_evento INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    lugar TEXT NOT NULL,
    sala TEXT NOT NULL,
    horario TEXT NOT NULL,
    tipo_pelicula TEXT NOT NULL,
    precio TEXT NOT NULL,
    nombre_pelicula TEXT NOT NULL 
)
'''
cursor.execute(crear_tabla_sql4)

crear_tabla_sql5 = '''
CREATE TABLE IF NOT EXISTS deporte (
    id_deporte INTEGER PRIMARY KEY,
    tipo_evento INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    lugar TEXT NOT NULL,
    juegan TEXT NOT NULL,
    posicion TEXT NOT NULL,
    precio TEXT NOT NULL,
    nombre_evento TEXT NOT NULL 
)
'''
cursor.execute(crear_tabla_sql5)

crear_tabla_sql6 = '''
CREATE TABLE IF NOT EXISTS concierto (
    id_concierto INTEGER PRIMARY KEY,
    tipo_evento INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    lugar TEXT NOT NULL,
    canta TEXT NOT NULL,
    genero TEXT NOT NULL,
    precio TEXT NOT NULL,
    nombre_evento TEXT NOT NULL 
)
'''
cursor.execute(crear_tabla_sql6)

conn.commit()
conn.close()