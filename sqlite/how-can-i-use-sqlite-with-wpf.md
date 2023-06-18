# How can I use SQLite with WPF?
// plain

SQLite is an open source relational database system that can be used with WPF (Windows Presentation Foundation) applications. To use SQLite with WPF, you must first install the SQLite ADO.NET provider. After that, you can create an application that establishes a connection to the SQLite database and executes SQL statements.

Here is an example of how to use SQLite with WPF:

```
using System;
using System.Data;
using System.Data.SQLite;

namespace SQLiteExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a connection to the SQLite database
            SQLiteConnection conn = new SQLiteConnection("Data Source=C:\\MyDatabase.db;Version=3;");

            // Open the connection
            conn.Open();

            // Create a command to execute
            SQLiteCommand cmd = new SQLiteCommand("SELECT * FROM customers", conn);

            // Execute the command and get the results
            SQLiteDataReader reader = cmd.ExecuteReader();

            // Iterate through the results
            while (reader.Read())
            {
                Console.WriteLine("Name: {0}", reader["name"]);
            }

            // Close the connection
            conn.Close();
        }
    }
}
```

This code will connect to the SQLite database located in the file `C:\MyDatabase.db` and execute a query to select all records from the `customers` table. It will then iterate through the results and output the `name` column from each record.

The code consists of the following parts:

1. Create a connection to the SQLite database: `SQLiteConnection conn = new SQLiteConnection("Data Source=C:\\MyDatabase.db;Version=3;");`
2. Open the connection: `conn.Open();`
3. Create a command to execute: `SQLiteCommand cmd = new SQLiteCommand("SELECT * FROM customers", conn);`
4. Execute the command and get the results: `SQLiteDataReader reader = cmd.ExecuteReader();`
5. Iterate through the results: `while (reader.Read())`
6. Output the `name` column from each record: `Console.WriteLine("Name: {0}", reader["name"]);`
7. Close the connection: `conn.Close();`

For more information, see the following links:

- [Using SQLite with WPF](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sqlite/using-sqlite-with-wpf)
- [SQLite ADO.NET Provider](https://system.data.sqlite.org/index.html/doc/trunk/www/downloads.wiki)

onelinerhub: [How can I use SQLite with WPF?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-wpf)