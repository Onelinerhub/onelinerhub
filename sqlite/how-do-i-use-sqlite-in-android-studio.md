# How do I use SQLite in Android Studio?
// plain

Using SQLite in Android Studio is a great way to store data for your app. To use SQLite in Android Studio, you'll need to add the SQLite library to your project. Here is an example of how to do this:

```
//Add the dependency to your project
implementation 'org.xerial:sqlite-jdbc:3.27.2.1'
```

Once the library is added, you can create a SQLiteDatabase object and use it to create tables and store data. Here is an example of how to do this:

```
//Create a SQLiteDatabase object
SQLiteDatabase db = SQLiteDatabase.openOrCreateDatabase("myDb.db", null);

//Create a table
String createTable = "CREATE TABLE IF NOT EXISTS myTable(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)";
db.execSQL(createTable);

//Insert data
String insertData = "INSERT INTO myTable(name) VALUES('John')";
db.execSQL(insertData);
```

You can also use the SQLiteDatabase object to query data. Here is an example of how to do this:

```
//Query data
String queryData = "SELECT * FROM myTable";
Cursor cursor = db.rawQuery(queryData, null);

//Iterate through the results
while(cursor.moveToNext()){
    String name = cursor.getString(1);
    Log.d("Name", name);
}

//Close the cursor
cursor.close();
```

The output of this code is:

```
D/Name: John
```

For more information on using SQLite in Android Studio, see the following links:

* [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-java/sqlite-jdbc/)
* [Android SQLite Database Tutorial](https://www.tutorialspoint.com/android/android_sqlite_database.htm)
* [Android SQLite Database Example](https://www.javatpoint.com/android-sqlite-database-example)

onelinerhub: [How do I use SQLite in Android Studio?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-in-android-studio)