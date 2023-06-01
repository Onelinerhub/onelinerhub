# m

How can I use the Elastica ORM with PHP?
// plain

The Elastica ORM is an object-relational mapping (ORM) library that provides a simple and elegant way to use Elasticsearch from PHP. It allows developers to write queries in a familiar SQL-like syntax while still taking advantage of the powerful search capabilities of Elasticsearch.

To use the Elastica ORM with PHP, you first need to install the library via Composer. You can do this by running the following command:

```
composer require elastica/elastica
```

Once the library is installed, you can create a connection to Elasticsearch and start using the ORM. An example of how to do this is shown below:

```php
<?php

use Elastica\Client;

$client = new Client([
    'host' => 'localhost',
    'port' => 9200
]);

$index = $client->getIndex('my_index');

// Use the ORM to perform queries against the index
```

The Elastica ORM provides a range of methods for performing queries against an Elasticsearch index, such as `search`, `count`, `get`, `update`, and `delete`. For example, you can use the `search` method to perform a full-text search on the index:

```php
<?php

$query = new \Elastica\Query\QueryString();
$query->setQuery('search term');

$resultSet = $index->search($query);

// Output the results
foreach($resultSet as $result) {
    echo $result->getData()['title'];
}
```

The Elastica ORM also provides a range of methods for manipulating documents in an index, such as `add`, `update`, and `delete`. For example, you can use the `add` method to add a document to the index:

```php
<?php

$document = new \Elastica\Document();
$document->setData([
    'title' => 'My Document',
    'content' => 'This is the content of my document'
]);

$index->addDocument($document);
```

The Elastica ORM is a powerful and easy-to-use library for working with Elasticsearch from PHP. For more information, please see the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [m

How can I use the Elastica ORM with PHP?](https://onelinerhub.com/php-elastica/m--how-can-i-use-the-elastica-orm-with-php)