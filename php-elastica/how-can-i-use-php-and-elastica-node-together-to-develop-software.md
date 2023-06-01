# How can I use PHP and Elastica Node together to develop software?
// plain

PHP and Elastica Node can be used together to develop software by creating a connection between them. This can be done by using a library such as Elastica-PHP, which provides an interface to connect to Elasticsearch from a PHP application.

## Example code

```php
<?php
require_once 'vendor/autoload.php';

$client = new Elastica\Client();
$index = $client->getIndex('my_index');

$type = $index->getType('my_type');
$doc = new Elastica\Document(1, array('name' => 'Hans'));
$type->addDocument($doc);
?>
```

The code above creates a connection between PHP and Elastica Node, and adds a document with a name of "Hans" to the index "my_index" and type "my_type".

Parts of the code:
- `require_once 'vendor/autoload.php'`: This line includes the autoloader to load the Elastica-PHP library.
- `$client = new Elastica\Client()`: This line creates an instance of the Elastica Client.
- `$index = $client->getIndex('my_index')`: This line creates an instance of the Elasticsearch index.
- `$type = $index->getType('my_type')`: This line creates an instance of the Elasticsearch type.
- `$doc = new Elastica\Document(1, array('name' => 'Hans'))`: This line creates a document with the ID of 1 and the name of "Hans".
- `$type->addDocument($doc)`: This line adds the document to the index.

## Helpful links
- [Elastica-PHP](https://github.com/ruflin/Elastica)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

onelinerhub: [How can I use PHP and Elastica Node together to develop software?](https://onelinerhub.com/php-elastica/how-can-i-use-php-and-elastica-node-together-to-develop-software)