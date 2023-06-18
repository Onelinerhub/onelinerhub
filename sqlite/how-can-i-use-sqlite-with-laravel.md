# How can I use SQLite with Laravel?
// plain

SQLite is a lightweight, open-source, relational database management system. It can be used with the Laravel web framework to store and manipulate data.

Using SQLite with Laravel is easy and straightforward. To get started, you first need to install the SQLite extension for PHP. Then, you can configure your Laravel application to use SQLite as its database by adding the following code to your `.env` file:

```
DB_CONNECTION=sqlite
```

Then, you can create your SQLite database file and configure it in your `config/database.php` file.

You can also interact with the database using the Eloquent ORM. You can create models and use the query builder to interact with the database. Here is an example of a query to get all records from a table:

```
$records = App\Record::all();
```

You can also use raw SQL queries to interact with the database. Here is an example of a query to select all records from a table:

```
$records = DB::select('SELECT * FROM records');
```

Using SQLite with Laravel is a great way to quickly get a database up and running for your application.

## Helpful links

- [SQLite Extension for PHP](https://www.php.net/manual/en/book.sqlite.php)
- [Configuring Your Database in Laravel](https://laravel.com/docs/7.x/database#configuration)
- [Eloquent ORM](https://laravel.com/docs/7.x/eloquent)
- [Raw SQL Queries in Laravel](https://laravel.com/docs/7.x/database#running-queries)

onelinerhub: [How can I use SQLite with Laravel?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-laravel)