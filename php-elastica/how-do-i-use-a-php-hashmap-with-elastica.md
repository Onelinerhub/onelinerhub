# How do I use a PHP hashmap with Elastica?
// plain

A hashmap is a data structure used to store and retrieve data quickly. In PHP, a hashmap can be used with Elastica to store and query documents.

To use a hashmap with Elastica, you need to create an instance of the `Elastica\Type\Mapping` class and then set the mapping type to `hashmap`. Then, you can use the `setProperties` method to define the fields and their types.

For example:
```
$mapping = new Elastica\Type\Mapping();
$mapping->setType('hashmap');
$mapping->setProperties(array(
    'name' => array('type' => 'string'),
    'age' => array('type' => 'integer'),
    'gender' => array('type' => 'keyword')
));
```

Once the mapping is set, you can use the `index` method to index the documents.

For example:
```
$doc1 = new Elastica\Document('1', array(
    'name' => 'John Doe',
    'age' => 30,
    'gender' => 'male'
));
$doc2 = new Elastica\Document('2', array(
    'name' => 'Jane Doe',
    'age' => 25,
    'gender' => 'female'
));
$type->index($doc1);
$type->index($doc2);
```

You can then use the `search` method to query the documents.

For example:
```
$query = new Elastica\Query\Match();
$query->setField('gender', 'female');
$results = $type->search($query);
```

This will return a list of documents that match the query.

## Helpful links
- [Elastica Documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [PHP Hashmap Documentation](https://www.php.net/manual/en/language.types.array.php)

onelinerhub: [How do I use a PHP hashmap with Elastica?](https://onelinerhub.com/php-elastica/how-do-i-use-a-php-hashmap-with-elastica)