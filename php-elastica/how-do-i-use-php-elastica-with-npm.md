# How do I use PHP Elastica with NPM?
// plain

**Using PHP Elastica with NPM**

PHP Elastica is an Elasticsearch client library for PHP and can be used in combination with NPM to build powerful search solutions. To use PHP Elastica with NPM, the following steps should be followed:

1. Install the Elasticsearch PHP plugin: `composer require elasticsearch/elasticsearch`

2. Install the PHP Elastica library: `composer require elastica/elastica`

3. Install the NPM package: `npm install elastica`

4. Create a `elasticsearch.php` file and include the following code to connect to the Elasticsearch instance:

```
<?php
require 'vendor/autoload.php';

$client = new \Elastica\Client();
```

5. Use the `elastica` NPM package to perform search operations. For example:

```
const elastica = require('elastica');

let query = new elastica.Query();
query.setQuery('title:example');

let search = client.search(query);

console.log(search);
```

## Output example

```
Elasticsearch\Endpoints\Search Object
(
    [params:protected] => Array
        (
            [index] =>
            [type] =>
            [body] => Array
                (
                    [query] => Array
                        (
                            [query_string] => Array
                                (
                                    [query] => title:example
                                )

                        )

                )

        )

)
```

By following these steps, PHP Elastica can be used in combination with NPM to build powerful search solutions.

## Helpful links

- [Elasticsearch PHP Plugin](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [PHP Elastica Library](https://github.com/ruflin/Elastica)
- [NPM Package](https://www.npmjs.com/package/elastica)

onelinerhub: [How do I use PHP Elastica with NPM?](https://onelinerhub.com/php-elastica/how-do-i-use-php-elastica-with-npm)