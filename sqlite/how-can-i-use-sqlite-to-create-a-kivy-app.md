# How can I use SQLite to create a Kivy app?
// plain

SQLite is a popular open source database engine that can be used to create Kivy apps. It is lightweight, self-contained, and requires no external dependencies. To use SQLite with Kivy, you need to install the [sqlite3](https://docs.python.org/2/library/sqlite3.html) module.

The following example code creates a Kivy app that uses SQLite to store data:

```python
import kivy
from kivy.app import App
from kivy.uix.button import Button
import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (name text, age integer)")

c.execute("INSERT INTO users VALUES ('John', 25)")

c.execute("SELECT * FROM users")
print(c.fetchall())

class MyApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ == '__main__':
    MyApp().run()
```

## Output example

```
[('John', 25)]
```

The code above does the following:
1. Imports the `kivy` and `sqlite3` modules.
2. Connects to an SQLite database called `my_database.db`.
3. Creates a table called `users` with two columns: `name` and `age`.
4. Inserts a row into the `users` table.
5. Queries the `users` table and prints the results.
6. Creates a Kivy app with a single button.
7. Runs the Kivy app.

onelinerhub: [How can I use SQLite to create a Kivy app?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-to-create-a-kivy-app)