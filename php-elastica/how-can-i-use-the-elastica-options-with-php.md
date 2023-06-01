# How can I use the Elastica options with PHP?
// plain

Using the Elastica options with PHP is relatively simple. The first step is to install the Elastica library. This can be done with composer:
```
composer require elastica/elastica
```

Once the library is installed, you can create a Client object which will allow you to interact with the Elasticsearch server:
```
$client = new \Elastica\Client([
    'host' => 'localhost',
    'port' => 9200
]);
```

Once the client is created, you can use the various methods available to interact with the Elasticsearch server. For example, you can create an index:
```
$index = $client->getIndex('my_index');
$index->create([
    'number_of_shards' => 4,
    'number_of_replicas' => 1
]);
```

You can also add documents to the index:
```
$doc = new \Elastica\Document(1, [
    'title' => 'My Document',
    'body' => 'This is the content of my document'
]);
$index->addDocument($doc);
```

You can also query the index:
```
$query = new \Elastica\Query\Match('title', 'document');
$results = $index->search($query);
```

These are just some of the operations that can be performed with the Elastica library. For more information, see the [Elastica documentation](https://github.com/ruflin/Elastica).

onelinerhub: [How can I use the Elastica options with PHP?](https://onelinerhub.com/php-elastica/how-can-i-use-the-elastica-options-with-php)