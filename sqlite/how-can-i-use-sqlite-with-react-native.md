# How can I use SQLite with React Native?
// plain

SQLite is an open source database technology that is used to store data in a relational manner. It is a popular choice for React Native applications as it is lightweight and can be embedded into the application itself. To use SQLite with React Native, you need to install the react-native-sqlite-storage package, which provides a JavaScript interface for SQLite.

To install the package, run the following command in the project directory:

```
npm install --save react-native-sqlite-storage
```

Once the package is installed, you can use it to create a SQLite database in your React Native application. The following example code creates a database called “mydb.db” and creates a table called “users”:

```
import SQLite from 'react-native-sqlite-storage';

let db = SQLite.openDatabase({name: 'mydb.db'});

db.transaction((tx) => {
 tx.executeSql('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50))');
});
```

This code will create a database with a single table named “users”. You can then use the SQLite API to perform operations on the database, such as inserting data into it, updating existing records, and querying the data.

Once you have created the database, you can use it to store and retrieve data from your React Native application. For example, the following code inserts a new user into the “users” table:

```
db.transaction((tx) => {
  tx.executeSql('INSERT INTO users (name) VALUES (?)', ['John Doe']);
});
```

This code will insert a new record with the name “John Doe” into the “users” table.

Using SQLite with React Native is a great way to store and manage data in a lightweight and efficient manner. With the react-native-sqlite-storage package, you can easily create and manage databases in your React Native applications.

## Helpful links

- [React Native SQLite Storage](https://github.com/andpor/react-native-sqlite-storage)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How can I use SQLite with React Native?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-react-native)