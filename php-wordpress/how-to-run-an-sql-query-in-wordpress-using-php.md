# How to run an SQL query in WordPress using PHP?
// plain

To run an SQL query in WordPress using PHP, you can use the `$wpdb` global object. This object provides a set of methods to interact with the WordPress database.

For example, to run a simple SELECT query:
```
$results = $wpdb->get_results( "SELECT * FROM {$wpdb->prefix}posts" );
```
This will return an array of objects containing the results of the query.

## Code explanation

- `$wpdb`: This is the global object that provides access to the WordPress database.
- `get_results()`: This is a method of the `$wpdb` object that is used to run a SELECT query.
- `$wpdb->prefix`: This is a property of the `$wpdb` object that contains the table prefix for the WordPress database.

## Helpful links
- [WordPress Database Description](https://codex.wordpress.org/WordPress_Database_Description)
- [$wpdb Class Reference](https://codex.wordpress.org/Class_Reference/wpdb)

onelinerhub: [How to run an SQL query in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-run-an-sql-query-in-wordpress-using-php)