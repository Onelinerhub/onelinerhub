# How can I connect to a MySQL database using Python and SSH?
// plain

You can connect to a MySQL database using Python and SSH by using a library called Paramiko. First, you need to install Paramiko on your machine. You can do this with `pip install paramiko`.

Once Paramiko is installed, you can use the following code to connect to your MySQL database via SSH:

```
import paramiko

# Create an SSH client
client = paramiko.SSHClient()

# Connect to the SSH server
client.connect(hostname='example.com', username='user', password='password')

# Execute a command on the SSH server
stdin, stdout, stderr = client.exec_command('mysql -u username -p database_name')

# Print the output of the command
print(stdout.read())
```

The code above will connect to the SSH server, execute the command `mysql -u username -p database_name`, and print the output of the command.

## Code explanation


1. `import paramiko`: This imports the Paramiko library.
2. `client = paramiko.SSHClient()`: This creates an SSH client.
3. `client.connect(hostname='example.com', username='user', password='password')`: This connects to the SSH server.
4. `stdin, stdout, stderr = client.exec_command('mysql -u username -p database_name')`: This executes the command `mysql -u username -p database_name` on the SSH server.
5. `print(stdout.read())`: This prints the output of the command.

Here are some ## Helpful links

- [Paramiko documentation](https://www.paramiko.org/docs/)
- [Connecting to a MySQL database using Python](https://www.w3schools.com/python/python_mysql_connect.asp)

onelinerhub: [How can I connect to a MySQL database using Python and SSH?](https://onelinerhub.com/python-mysql/how-can-i-connect-to-a-mysql-database-using-python-and-ssh)