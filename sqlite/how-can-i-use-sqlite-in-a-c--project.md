# How can I use SQLite in a C# project?
// plain

SQLite is a lightweight database that can be used in C# projects. It is a self-contained, serverless, zero-configuration, transactional SQL database engine. To use SQLite in a C# project, you need to install the NuGet package for the System.Data.SQLite library.

Once the NuGet package is installed, you can use the following example code to create a database and table:

```
using System;
using System.Data.SQLite;

namespace SQLiteExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a connection to the database
            SQLiteConnection connection = new SQLiteConnection("Data Source=database.db;Version=3;");
            connection.Open();

            // Create a table
            string sql = "CREATE TABLE IF NOT EXISTS Highscores (name VARCHAR(20), score INT)";
            SQLiteCommand command = new SQLiteCommand(sql, connection);
            command.ExecuteNonQuery();

            // Close connection
            connection.Close();
        }
    }
}
```

This code will create a database file called `database.db` and a table called `Highscores` with two columns (`name` and `score`).

The code consists of the following parts:
1. `using System;` and `using System.Data.SQLite;` - These lines import the necessary libraries.
2. `SQLiteConnection connection = new SQLiteConnection("Data Source=database.db;Version=3;");` - This creates a connection to the SQLite database.
3. `string sql = "CREATE TABLE IF NOT EXISTS Highscores (name VARCHAR(20), score INT)";` - This creates a SQL command to create the `Highscores` table.
4. `SQLiteCommand command = new SQLiteCommand(sql, connection);` - This creates a command object with the SQL command and connection.
5. `command.ExecuteNonQuery();` - This executes the SQL command.
6. `connection.Close();` - This closes the connection to the database.

For more information, see the following links:
- [System.Data.SQLite](https://system.data.sqlite.org/index.html/doc/trunk/www/index.wiki)
- [Getting Started with SQLite and C#](https://www.tutorialspoint.com/sqlite/sqlite_csharp.htm)

onelinerhub: [How can I use SQLite in a C# project?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-in-a-c--project)