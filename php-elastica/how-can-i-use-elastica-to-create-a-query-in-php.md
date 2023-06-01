# How can I use Elastica to create a query in PHP?
// plain

Elastica is a PHP client library for the popular open source search engine, Elasticsearch. It provides an easy to use API for creating and executing queries against an Elasticsearch cluster.

To create a query in PHP using Elastica, you can use the `Search` class. The `Search` class provides methods for building and executing queries.

For example, the following code snippet creates a query and executes it against an Elasticsearch cluster:

```php
$client = new \Elastica\Client();
$search = new \Elastica\Search($client);
$query = new \Elastica\Query\MatchAll();
$resultSet = $search->search($query);
```

The code above creates a new Elastica client, creates a new search object using the client, creates a new MatchAll query, and then executes the query.

The `$resultSet` variable will contain the results of the query. It is an instance of `Elastica\ResultSet`, which contains the total number of hits and the results of the query.

## Code explanation


1. `$client = new \Elastica\Client();`: creates a new Elastica client.
2. `$search = new \Elastica\Search($client);`: creates a new search object using the client.
3. `$query = new \Elastica\Query\MatchAll();`: creates a new MatchAll query.
4. `$resultSet = $search->search($query);`: executes the query and stores the results in the `$resultSet` variable.

## Helpful links

- [Elastica documentation](https://elastica.io/docs/index.html)
- [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How can I use Elastica to create a query in PHP?](https://onelinerhub.com/php-elastica/how-can-i-use-elastica-to-create-a-query-in-php)