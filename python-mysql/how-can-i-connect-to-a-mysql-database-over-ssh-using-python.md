# How can I connect to a MySQL database over SSH using Python?
// plain

You can connect to a MySQL database over SSH using Python with the help of a library such as Paramiko.

First, you need to install Paramiko:
```
pip install paramiko
```

Then, you can create a SSH client and connect to the server:
```
import paramiko

hostname = 'example.com'
port = 22
username = 'username'
password = 'password'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)
```

After the connection is established, you can use the Paramiko client to execute commands on the server, such as `mysql -u username -p` to connect to the MySQL database.

You can also use a library such as MySQL Connector to execute SQL queries directly on the database. To do this, you need to create a SSH tunnel and pass the tunnel information to MySQL Connector:

```
import paramiko
import mysql.connector

hostname = 'example.com'
port = 22
username = 'username'
password = 'password'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)

transport = client.get_transport()
local_port = 3306
dest_addr = '127.0.0.1'
dest_port = 3306

channel = transport.open_channel("direct-tcpip", (dest_addr, dest_port), ('127.0.0.1', local_port))

db = mysql.connector.connect(host='127.0.0.1', port=local_port, user='username', password='password', database='database')
```

After the tunnel is established, you can use the `db` object to execute SQL queries on the database.

**List of code parts with detailed explanation**

1. `pip install paramiko` - Installs Paramiko library.
2. `import paramiko` - Imports the Paramiko library.
3. `client = paramiko.SSHClient()` - Creates a SSH client.
4. `client.set_missing_host_key_policy(paramiko.AutoAddPolicy())` - Sets the missing host key policy to AutoAddPolicy.
5. `client.connect(hostname, port, username, password)` - Connects to the server.
6. `transport = client.get_transport()` - Gets the transport from the client.
7. `channel = transport.open_channel("direct-tcpip", (dest_addr, dest_port), ('127.0.0.1', local_port))` - Opens a SSH channel.
8. `db = mysql.connector.connect(host='127.0.0.1', port=local_port, user='username', password='password', database='database')` - Connects to the MySQL database.

**Relevant links**

- Paramiko documentation: https://www.paramiko.org/
- MySQL Connector documentation: https://dev.mysql.com/doc/connector-python/en/

onelinerhub: [How can I connect to a MySQL database over SSH using Python?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-a-mysql-database-over-ssh-using-python)