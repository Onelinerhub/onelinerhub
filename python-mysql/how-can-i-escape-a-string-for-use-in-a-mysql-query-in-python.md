# How can I escape a string for use in a MySQL query in Python?
// plain

Escaping a string for use in a MySQL query in Python can be done using the `MySQLdb.escape_string()` function. This function takes a string as an argument and returns an escaped version of the string, with any special characters such as single quotes, double quotes, backslashes, etc. replaced with their escaped equivalents.

For example, the following code block:

```
import MySQLdb

myString = "This string contains 'single quotes' and \"double quotes\""

escapedString = MySQLdb.escape_string(myString)

print(escapedString)
```

will output:

```
This string contains \'single quotes\' and \"double quotes\"
```

The code works by:

1. Importing the `MySQLdb` module
2. Assigning a string to the `myString` variable
3. Passing the `myString` variable to the `MySQLdb.escape_string()` function
4. Assigning the returned value to the `escapedString` variable
5. Printing the `escapedString` variable

For more information, see the [MySQLdb documentation](https://mysqlclient.readthedocs.io/user_guide.html#escaping-strings).

onelinerhub: [How can I escape a string for use in a MySQL query in Python?](https://onelinerhub.com/python-mysql/how-can-i-escape-a-string-for-use-in-a-mysql-query-in-python)