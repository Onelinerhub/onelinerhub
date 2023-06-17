# ¿Cómo conectar Python a MySQL usando ejemplos?
// plain

Para conectar Python a MySQL, primero hay que instalar el módulo de Python MySQL. Esto se puede hacer usando el administrador de paquetes pip. Una vez instalado, un ejemplo de código para conectar Python a MySQL es el siguiente:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="usuario",
  passwd="contraseña"
)

print(mydb)
```

Esto imprimirá el objeto `mydb` que se usa para realizar operaciones en la base de datos. Para ejecutar consultas, se usa el método `execute()` sobre el objeto `mydb`. Por ejemplo, para ejecutar la consulta `SELECT * FROM tabla`:

```
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tabla")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

Esto imprimirá todas las filas de la tabla.

Lista de partes del código y explicación:

- `mysql.connector`: El módulo de Python que se usa para conectar Python a MySQL.
- `mydb = mysql.connector.connect()`: Esta línea se usa para conectar Python a MySQL.
- `host`, `user`, `passwd`: Estos son los parámetros necesarios para conectar Python a MySQL.
- `mycursor = mydb.cursor()`: Esta línea se usa para crear un objeto `cursor` que se usa para ejecutar consultas.
- `mycursor.execute("SELECT * FROM tabla")`: Esta línea se usa para ejecutar una consulta SQL.
- `myresult = mycursor.fetchall()`: Esta línea se usa para obtener los resultados de la consulta.
- `for x in myresult:`: Esta línea se usa para iterar sobre los resultados.

Enlaces relevantes:

- [Documentación de Python MySQL](https://dev.mysql.com/doc/connector-python/en/)
- [Tutorial de Python MySQL](https://www.w3schools.com/python/python_mysql.asp)

onelinerhub: [¿Cómo conectar Python a MySQL usando ejemplos?](https://onelinerhub.com/python-mysql/--c--mo-conectar-python-a-mysql-usando-ejemplos)