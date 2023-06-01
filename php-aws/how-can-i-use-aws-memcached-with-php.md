# How can I use AWS Memcached with PHP?
// plain

Using AWS Memcached with PHP is easy and straightforward.

First, you will need to install the [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/) and [Memcached for PHP](http://php.net/manual/en/book.memcached.php).

Once the SDK and Memcached are installed, you can use the following code to connect to your AWS Memcached instance:

```php
<?php

$client = new Aws\ElastiCache\ElastiCacheClient([
    'region' => 'us-east-1',
    'version' => 'latest',
]);

$result = $client->describeCacheClusters([
    'CacheClusterId' => 'my-memcached-cluster',
]);

$endpoint = $result['CacheClusters'][0]['ConfigurationEndpoint']['Address'];

$memcached = new Memcached();
$memcached->addServer($endpoint, 11211);

$memcached->set('key', 'value');

echo $memcached->get('key'); // Output: value

?>
```

This code will connect to your Memcached instance, set the key `key` to the value `value`, and then output the value of `key`.

You can also use the AWS SDK for PHP to access other features of your Memcached instance, such as creating snapshots, managing security groups, and more. For more information, see the [AWS ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/latest/mem-ug/).

onelinerhub: [How can I use AWS Memcached with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-aws-memcached-with-php)