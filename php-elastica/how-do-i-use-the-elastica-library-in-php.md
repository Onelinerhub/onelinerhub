# How do I use the Elastica library in PHP?
// plain

The Elastica library is a powerful tool for quickly and easily connecting to and managing Elasticsearch from PHP. It provides a simple and intuitive interface for creating, updating, and deleting documents, as well as running queries and aggregations.

To use the Elastica library in PHP, first install it with Composer:

```
composer require elastica/elastica
```

Then, create an instance of the `Elastica\Client` class, passing in an array of configuration parameters:

```php
$config = [
    'host' => 'localhost',
    'port' => 9200,
];
$client = new \Elastica\Client($config);
```

Once the client is created, you can use it to interact with Elasticsearch. For example, to create an index:

```php
$index = $client->getIndex('my_index');
$index->create(['settings' => ['number_of_shards' => 1]]);
```

Or, to index a document:

```php
$doc = new \Elastica\Document(1, ['name' => 'John Doe']);
$index->addDocument($doc);
```

For more information on the Elastica library, please see the [documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How do I use the Elastica library in PHP?](https://onelinerhub.com/php-elastica/how-do-i-use-the-elastica-library-in-php)