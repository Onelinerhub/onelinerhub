# How do I create a Python script to back up my MySQL database?
// plain

Creating a Python script to back up your MySQL database is a simple process. Here is an example of the code needed to do so:

```
# Import the MySQLdb module
import MySQLdb

# Connect to the database
db = MySQLdb.connect("hostname","username","password","database_name")

# Create a cursor object
cursor = db.cursor()

# Execute the SQL command to backup the database
cursor.execute("mysqldump -u username -p database_name > database_name.sql")

# Disconnect from the database
db.close()
```

## Code explanation


* `import MySQLdb` - Imports the module needed to connect to the MySQL database.

* `db = MySQLdb.connect("hostname","username","password","database_name")` - Connects to the MySQL database.

* `cursor = db.cursor()` - Creates a cursor object to execute the SQL command.

* `cursor.execute("mysqldump -u username -p database_name > database_name.sql")` - Executes the SQL command to back up the database.

* `db.close()` - Disconnects from the database.

For more information on how to create a Python script to back up your MySQL database, please see the following links:

* [MySQL Backup and Restore using Python](https://www.mysqltutorial.org/mysql-backup-and-restore-using-python/)
* [How To Back Up MySQL Databases from the Command Line](https://www.digitalocean.com/community/tutorials/how-to-back-up-mysql-databases-from-the-command-line)

onelinerhub: [How do I create a Python script to back up my MySQL database?](https://onelinerhub.com/python-mysql/how-do-i-create-a-python-script-to-back-up-my-mysql-database)