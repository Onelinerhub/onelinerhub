# How can I use PHP to integrate with Elasticsearch?
// plain

You can use PHP to integrate with Elasticsearch by using the official [Elasticsearch Client Library for PHP](https://github.com/elastic/elasticsearch-php). This library allows you to communicate with an Elasticsearch cluster from your PHP application.

For example, the following code connects to an Elasticsearch cluster and returns a list of all indices:

```php
<?php
require 'vendor/autoload.php';

$hosts = [
    '127.0.0.1:9200' // IP + Port
];

$client = Elasticsearch\ClientBuilder::create()->setHosts($hosts)->build();

$params = [
    'index' => '_all'
];

$response = $client->cat()->indices($params);

echo $response;
```

The output of this code will be a list of all the indices in your cluster:

```
health status index uuid pri rep docs.count docs.deleted store.size pri.store.size
``

The library also allows you to perform other operations, such as creating, updating and deleting indices and documents, as well as searching and aggregating data. For more information, see the [documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How can I use PHP to integrate with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-php-to-integrate-with-elasticsearch)