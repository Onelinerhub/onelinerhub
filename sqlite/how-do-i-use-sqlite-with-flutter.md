# How do I use SQLite with Flutter?
// plain

Using SQLite with Flutter is a very simple process. Here is an example of how to use it:

```dart
import 'package:sqflite/sqflite.dart';

//get a database
var db = await openDatabase('my_db.db');

//create a table
await db.execute('CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT, value INTEGER, num REAL)');

//insert some data
int id1 = await db.rawInsert('INSERT INTO my_table(name, value, num) VALUES("some name", 1234, 456.789)');

//query the database
List<Map> list = await db.rawQuery('SELECT * FROM my_table');

//update some data
int count = await db.rawUpdate('UPDATE my_table SET name = ?, VALUE = ? WHERE name = ?', ['new name', '9876', 'some name']);

//delete data
int count = await db.rawDelete('DELETE FROM my_table WHERE name = ?', ['some name']);

//close database
db.close();
```

Above code will:
1. Open a database connection with `openDatabase`
2. Create a table with `execute`
3. Insert data with `rawInsert`
4. Query the database with `rawQuery`
5. Update data with `rawUpdate`
6. Delete data with `rawDelete`
7. Close the database connection with `close`

## Helpful links
- [Sqflite Documentation](https://pub.dev/documentation/sqflite/latest/)
- [Flutter SQLite Tutorial](https://flutter.dev/docs/cookbook/persistence/sqlite)

onelinerhub: [How do I use SQLite with Flutter?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-with-flutter)