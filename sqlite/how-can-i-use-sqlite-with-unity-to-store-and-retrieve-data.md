# How can I use SQLite with Unity to store and retrieve data?
// plain

SQLite is a lightweight, open-source, relational database management system that can be used with Unity to store and retrieve data. It is fast, reliable, and requires minimal setup.

To use SQLite with Unity, you will need to install the [SQLite4Unity3d](https://github.com/robertohuertasm/SQLite4Unity3d) library.

Once installed, you can create a database connection and execute queries. For example:

```
// Create a connection to the database
SQLiteConnection connection = new SQLiteConnection("MyDatabase.db");

// Execute a query
SQLiteCommand command = connection.CreateCommand("SELECT * FROM MyTable");

// Retrieve the results
SQLiteDataReader reader = command.ExecuteReader();

// Loop through the results
while (reader.Read())
{
    string name = reader.GetString(0);
    int age = reader.GetInt32(1);
    Debug.Log($"Name: {name}, Age: {age}");
}
```

This example will connect to a database called `MyDatabase.db` and execute a query to select all records from a table called `MyTable`. The results are then looped through and each record is printed to the console.

For more information, see the [SQLite4Unity3d documentation](https://github.com/robertohuertasm/SQLite4Unity3d/wiki).

onelinerhub: [How can I use SQLite with Unity to store and retrieve data?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-unity-to-store-and-retrieve-data)