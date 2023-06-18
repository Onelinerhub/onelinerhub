# How do I use SQLite in an Android application?
// plain

Using SQLite in an Android application is an easy way to store data locally. It is a light-weight database that is built into the Android OS and can be used to store structured data.

The following is an example of how to create a database and a table in SQLite and insert some data into it:

```java
// Create a database
SQLiteDatabase db = openOrCreateDatabase("myDB", MODE_PRIVATE, null);

// Create a table
db.execSQL("CREATE TABLE IF NOT EXISTS myTable (name VARCHAR, age INT(3))");

// Insert data
db.execSQL("INSERT INTO myTable (name, age) VALUES ('John', 30)");
```

Once the data has been inserted, it can be queried using the `SELECT` statement:

```java
// Query the data
Cursor cursor = db.rawQuery("SELECT * FROM myTable", null);

// Iterate through the result set
while (cursor.moveToNext()) {
    String name = cursor.getString(0);
    int age = cursor.getInt(1);
    Log.d("Database", "Name: " + name + ", Age: " + age);
}
```

The output would be:

```
D/Database: Name: John, Age: 30
```

## Code explanation

1. `openOrCreateDatabase` - opens or creates a database with the given name and mode
2. `db.execSQL` - executes an SQL statement
3. `rawQuery` - executes a query and returns a `Cursor` object
4. `cursor.moveToNext` - moves the cursor to the next row
5. `cursor.getString` - returns the value of the given column index as a `String`
6. `cursor.getInt` - returns the value of the given column index as an `int`
7. `Log.d` - writes a log message

## Helpful links
- [Android SQLite Tutorial](https://www.tutorialspoint.com/android/android_sqlite_database.htm)
- [SQLite Database Tutorial](https://www.tutorialspoint.com/sqlite/sqlite_overview.htm)

onelinerhub: [How do I use SQLite in an Android application?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-in-an-android-application)