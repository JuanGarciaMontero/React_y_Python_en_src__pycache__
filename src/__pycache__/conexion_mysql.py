import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database_python" # Debe existir para colocarla aqui, y ojo con la coma anterior.
)
# Saber si hay conexion -> print(mydb)
mycursor = mydb.cursor() # Variable que recoje el metodo cursor de mydb. SIEMPRE SE USA

# Crear la base de datos -> mycursor.execute("CREATE DATABASE database_python")
# Mostrar las Bases de Datos de Mysql -> mycursor.execute("SHOW DATABASES")

# Recorrer todas las Bases de Datos de Mysql -> for x in mycursor:
  # Imprimir por terminal de panalla dodas las bases de datos recorridas -> print(x)

# Crear tabla personas con los campos 'name' y adress' -> mycursor.execute("CREATE TABLE personas (name VARCHAR(255), address VARCHAR(255))")

# Alterar la tabla personas añadiendo el campo 'id' -> mycursor.execute("ALTER TABLE personas ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insertar un registro nuevo en la tabla personas -> sql = "INSERT INTO personas (name, address) VALUES (%s, %s)"
# val = ("Juan", "C/ Almendro, 20")

# Ejecotar la sentencia mysql -> mycursor.execute(sql, val)

# Sino no muestra la insercion echa (es como un refresco de la base de datos) ->mydb.commit()

# Imprimir por terminal si el número de fila inseertada y que se ha grabado la insercion -> print(mycursor.rowcount, "record inserted.")

# Sentencia SQL recogida en la variable 'sql' -> sql = "INSERT INTO personas (name, address) VALUES (%s, %s)"
""" Nombre y direcciones, recogido en un array y guaradado en la variable 'val' -> val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]"""

# Método, para insertar varias filas en una tabla -> mycursor.executemany(sql, val)

# Actualizacion Base de datos -> mydb.commit()

# Imprimir -> print(mycursor.rowcount, "was inserted.")
# imprime la ultima fila insertada -> print("1 record inserted, ID:", mycursor.lastrowid)

"""mycursor.execute("SELECT * FROM personas")

myresult = mycursor.fetchall() # Se usa el método fetchall que recoje todas las filas de la última declaración SQL

for x in myresult: # Iteración que recorre a través de la variable 'x' todo el contenido en 'myresult'
  print(x)"""   # Imprime cada una de las variable 'x' de la iteración de la variable 'myresult'

# Método que devuelve la primera fila del resultado -> myresult = mycursor.fetchone()

# Imprime lo que hay dentro de la variable 'myresult' -> print(myresult)

""" Consulta de de la tabla de todos los datos con la restricción WHERE -> sql = "SELECT * FROM personas WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)"""

""" Selecionar todo de la tabla persona ordenadas por 'name', por defecto ASC si es al revés poner 'DESC' -> sql = "SELECT * FROM personas ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)"""

""" Borrar del a tabla personas aquellas que tengna una determinada 'address' -> sql = "DELETE FROM personas WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")"""

""" Borra tabla -> sql = "DROP TABLE customers"

mycursor.execute(sql)"""

""" Borra tabla si exite -> sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)"""

""" Actualizacion de la tabla -> sql = "UPDATE personas SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")"""

""" Seleccionar con un limite de 5 registros o filas ->mycursor.execute("SELECT * FROM personas LIMIT 5")
# Limite 5 comenzando en el registro 2, imprime del registro 3 al 7 -> mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)"""
  
""" Unir dos tablas, tabla usuario y tabla productos, nuebla tabla llamada 'products', y donde 'users.fav' = 'products.id' -> sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"""
  
