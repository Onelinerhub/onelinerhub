# How can I use SQLite with WebAssembly?
// plain

Using SQLite with WebAssembly is possible by making use of the [SQLite3 WebAssembly Build](https://github.com/kripken/sql.js). It allows you to compile the SQLite library to WebAssembly and use it in web applications.

To use SQLite with WebAssembly, you will need to include the following code in your HTML file:

```html
<script src="sql.js"></script>
<script>
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'my_database.sqlite', true);
  xhr.responseType = 'arraybuffer';

  xhr.onload = function(e) {
    var uInt8Array = new Uint8Array(this.response);
    var db = new SQL.Database(uInt8Array);
  };
  xhr.send();
</script>
```

This code loads the SQLite database file into a `Uint8Array` object, which is then used to create an instance of the `SQL.Database` class. This instance can be used to execute SQL queries on the database.

For example, the following code can be used to execute a SELECT query on the database:

```javascript
var stmt = db.prepare('SELECT * FROM my_table');
while (stmt.step()) {
  var row = stmt.getAsObject();
  console.log(row);
}
```

The output of this code would be the rows returned from the query, each one printed to the console.

## Helpful links

- [SQLite3 WebAssembly Build](https://github.com/kripken/sql.js)
- [Using SQLite with WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly/Using_the_JavaScript_API_for_SQLite)

onelinerhub: [How can I use SQLite with WebAssembly?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-webassembly)