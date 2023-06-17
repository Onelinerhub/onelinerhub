# How can I create a web page using Python, MySQL, and HTML?
// plain

Creating a web page using Python, MySQL, and HTML requires several steps.

First, you must create a database in MySQL. The following code creates a database called “mywebpage”:

```
CREATE DATABASE mywebpage;
```

Next, create a table in the database to store web page information. The following code creates a table called “pages”:

```
CREATE TABLE pages (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (id)
);
```

Once the database and table have been created, you must use Python to connect to the database and execute SQL queries. The following code connects to the database and inserts a row into the “pages” table:

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mywebpage"
)

mycursor = mydb.cursor()

sql = "INSERT INTO pages (title, content) VALUES (%s, %s)"
val = ("My Web Page", "This is my web page content.")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

## Output example


```
1 record inserted.
```

Once the data has been inserted into the database, you must use HTML to create the web page. The following code creates a basic web page with a title and content:

```
<html>
    <head>
        <title>My Web Page</title>
    </head>
    <body>
        <h1>My Web Page</h1>
        <p>This is my web page content.</p>
    </body>
</html>
```

## Code explanation


1. MySQL code to create a database and table.
2. Python code to connect to the database and execute SQL queries.
3. HTML code to create the web page.

## Helpful links

- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)
- [HTML Tutorial](https://www.w3schools.com/html/)

onelinerhub: [How can I create a web page using Python, MySQL, and HTML?](https://onelinerhub.com/python-mysql/how-can-i-create-a-web-page-using-python--mysql--and-html)