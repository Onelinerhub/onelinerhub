# How do I use PHP Elastica to create an index?
// plain

1. First, install the Elastica library into your project using composer: `composer require "elastica/elastica:~2.0"`

2. Next, create a new `\Elastica\Client` instance and set the connection parameters for the Elasticsearch server:
```php
$client = new \Elastica\Client(['host' => 'localhost', 'port' => 9200]);
```

3. Then, create an index with the desired settings:
```php
$index = $client->getIndex('my_index');
$index->create(array(
    'number_of_shards' => 3,
    'number_of_replicas' => 2
), true);
```

4. Finally, add documents to the index:
```php
$doc1 = new \Elastica\Document(1, array('title' => 'Foo', 'content' => 'Foo bar'));
$doc2 = new \Elastica\Document(2, array('title' => 'Bar', 'content' => 'Bar foo'));
$docs = array($doc1, $doc2);

$index->addDocuments($docs);
```

5. You can then check the index status with:
```php
$status = $index->getStatus();
echo $status->getNumberOfDocuments(); // Outputs: 2
```

6. To learn more about creating and managing indexes with Elastica, refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

7. You can also find more detailed examples in the [Elastica GitHub repository](https://github.com/ruflin/Elastica).

onelinerhub: [How do I use PHP Elastica to create an index?](https://onelinerhub.com/php-elastica/how-do-i-use-php-elastica-to-create-an-index)