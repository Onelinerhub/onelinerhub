# How can I use the PHP Elastica API to query data?
// plain

The PHP Elastica API can be used to query data in an Elasticsearch index. Queries can be constructed using the `Search` object and the `Query` object.

## Example


```php
<?php

// include the Elastica lib
require_once 'path/to/elastica/lib/Elastica/Autoloader.php';
Elastica\Autoloader::register();

// create an instance of the Elastica client
$client = new Elastica\Client();

// create a search object
$search = new Elastica\Search($client);

// create a query object
$query = new Elastica\Query();

// set the query string
$query->setQueryString('example');

// set the index to search
$search->addIndex('my_index');

// set the type to search
$search->addType('my_type');

// execute the query
$results = $search->search($query);

// print the results
print_r($results);

```

## Output example

```php
Elastica\ResultSet Object
(
    [_results:protected] => Array
        (
            [0] => Elastica\Result Object
                (
                    [_data:protected] => Array
                        (
                            [_index] => my_index
                            [_type] => my_type
                            [_id] => 1
                            [_score] => 1
                            [_source] => Array
                                (
                                    [field1] => value1
                                    [field2] => example
                                    [field3] => value3
                                )

                        )

                )

        )

)
```

The code above:
- includes the Elastica library (`require_once 'path/to/elastica/lib/Elastica/Autoloader.php';`)
- creates an instance of the Elastica client (`$client = new Elastica\Client();`)
- creates a search object (`$search = new Elastica\Search($client);`)
- creates a query object (`$query = new Elastica\Query();`)
- sets the query string (`$query->setQueryString('example');`)
- sets the index to search (`$search->addIndex('my_index');`)
- sets the type to search (`$search->addType('my_type');`)
- executes the query (`$results = $search->search($query);`)
- prints the results (`print_r($results);`)

## Helpful links
- [Elasticsearch - PHP Client](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [Elastica - PHP Client](https://github.com/ruflin/Elastica)

onelinerhub: [How can I use the PHP Elastica API to query data?](https://onelinerhub.com/php-elastica/how-can-i-use-the-php-elastica-api-to-query-data)