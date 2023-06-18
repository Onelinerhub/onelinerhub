# How can I use SQLite with Xamarin Forms?
// plain

SQLite is a popular open source database engine that can be used with Xamarin Forms. To use it, you must first install the SQLite.Net-PCL NuGet package.

```
Install-Package sqlite-net-pcl
```

Then, you can create a SQLiteConnection object to access the database.

```
var db = new SQLiteConnection("MyDatabase.db3");
```

You can then use this connection to create tables, insert data, query data, and delete data. For example, to create a table, you can use the CreateTable method.

```
db.CreateTable<Person>();
```

You can also use the Insert method to insert data into a table.

```
db.Insert(new Person { Name = "John", Age = 20 });
```

To query data from the table, you can use the Table method.

```
var people = db.Table<Person>().ToList();
```

Finally, you can use the Delete method to delete data from the table.

```
db.Delete(person);
```

For more information, refer to the [SQLite.Net-PCL documentation](https://github.com/praeclarum/sqlite-net) and the [Xamarin documentation](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/data-cloud/data/databases).

onelinerhub: [How can I use SQLite with Xamarin Forms?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-xamarin-forms)