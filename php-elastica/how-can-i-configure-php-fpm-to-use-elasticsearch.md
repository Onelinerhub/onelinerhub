# How can I configure php-fpm to use elasticsearch?
// plain

To configure php-fpm to use elasticsearch, you need to install the PHP Elasticsearch Client. This can be done using composer by running the following command:
```
composer require elasticsearch/elasticsearch
```
Once the client is installed, you can use it to connect to your Elasticsearch instance. For example:
```
$client = new \Elasticsearch\Client(array(
    'hosts' => array('localhost:9200')
));
```
This will create a new client instance that can be used to interact with your Elasticsearch instance.

To use the client, you need to include the autoloader in your PHP script. For example:
```
require 'vendor/autoload.php';
```

Once the autoloader is included, you can use the client to interact with your Elasticsearch instance. For example:
```
$params = [
    'index' => 'my_index',
    'type' => 'my_type',
    'body' => [
        'query' => [
            'match' => [
                'title' => 'Elasticsearch'
            ]
        ]
    ]
];

$results = $client->search($params);
```

This code will search the `my_index` index for documents with the title `Elasticsearch`. The results will be stored in the `$results` variable.

## Helpful links
- [Elasticsearch PHP Client](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [Composer](https://getcomposer.org/)

onelinerhub: [How can I configure php-fpm to use elasticsearch?](https://onelinerhub.com/php-elastica/how-can-i-configure-php-fpm-to-use-elasticsearch)