# How do I use the Elastica library to join two tables in PHP?
// plain

The Elastica library is a PHP library that provides a powerful set of tools for creating and querying Elasticsearch databases. It can be used to join two tables in PHP by using the `addJoin` method. The `addJoin` method takes three parameters: the type of join, the name of the field in the first table, and the name of the field in the second table.

For example, the following code snippet shows how to join two tables, `users` and `orders`, using an inner join on the `user_id` field in both tables:

```
$query = new \Elastica\Query();
$query->addJoin('inner', 'users.user_id', 'orders.user_id');
```

The code above will create a query that will join the two tables, `users` and `orders`, on the `user_id` field in both tables.

## Code explanation


- `$query = new \Elastica\Query();`: This line creates a new instance of the `Elastica\Query` class.

- `$query->addJoin('inner', 'users.user_id', 'orders.user_id');`: This line adds a join to the query, specifying the type of join (in this case, `inner`), and the field names in both tables to join on (in this case, `users.user_id` and `orders.user_id`).

## Helpful links

- [Elastica Documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [Elastica GitHub Repository](https://github.com/ruflin/Elastica)

onelinerhub: [How do I use the Elastica library to join two tables in PHP?](https://onelinerhub.com/php-elastica/how-do-i-use-the-elastica-library-to-join-two-tables-in-php)