# How do I hide a MySQL password when using Python?
// plain

To hide a MySQL password when using Python, you can use the getpass module. This module allows you to prompt the user for a password without echoing it to the screen. Here is an example code block that demonstrates how to use the getpass module:

```
import getpass

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

print("Username:", username)
print("Password:", password)
```

When the code is executed, it will prompt the user for a username and password, but the password will not be echoed to the screen.

Parts of the code:

* `import getpass`: This imports the getpass module.
* `username = input("Enter username: ")`: This prompts the user for a username and stores it in the `username` variable.
* `password = getpass.getpass("Enter password: ")`: This prompts the user for a password and stores it in the `password` variable. The password will not be echoed to the screen.
* `print("Username:", username)`: This prints the username to the screen.
* `print("Password:", password)`: This prints the password to the screen.

## Helpful links

* [getpass — Portable Password Input — Python 3.9.1 documentation](https://docs.python.org/3/library/getpass.html)

onelinerhub: [How do I hide a MySQL password when using Python?](https://onelinerhub.com/python-mysql/how-do-i-hide-a-mysql-password-when-using-python)