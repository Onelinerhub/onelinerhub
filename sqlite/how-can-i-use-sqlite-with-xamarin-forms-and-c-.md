# How can I use SQLite with Xamarin Forms and C#?
// plain

SQLite is a lightweight database that can be used with Xamarin Forms and C# to store data. To use SQLite with Xamarin Forms and C#, the following steps should be taken:

1. Install the SQLite-net-pcl NuGet package in the shared project.
2. Create a class to represent the data model and add the attributes required to store the data.
3. Create a Database class with a single method to create the database.
4. Create a DatabaseService class with methods to perform CRUD operations on the database.
5. Call the DatabaseService methods from the shared project.

## Example code

```c#
// Create a class to represent the data model
public class User
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
}

// Create a Database class with a single method to create the database
public class Database
{
    public static SQLiteAsyncConnection CreateDatabase()
    {
        return new SQLiteAsyncConnection("database.db");
    }
}

// Create a DatabaseService class with methods to perform CRUD operations on the database
public class DatabaseService
{
    private SQLiteAsyncConnection _database;

    public DatabaseService()
    {
        _database = Database.CreateDatabase();
        _database.CreateTableAsync<User>();
    }

    public Task<int> InsertUser(User user)
    {
        return _database.InsertAsync(user);
    }

    public Task<List<User>> GetUsers()
    {
        return _database.Table<User>().ToListAsync();
    }
}
```

## Helpful links
- [SQLite-net-pcl NuGet package](https://www.nuget.org/packages/sqlite-net-pcl/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Xamarin Documentation](https://docs.microsoft.com/en-us/xamarin/)

onelinerhub: [How can I use SQLite with Xamarin Forms and C#?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-xamarin-forms-and-c-)