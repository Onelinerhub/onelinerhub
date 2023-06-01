# How can I use PHP to connect to an Amazon Web Services Elasticache instance?
// plain

Connecting to an Amazon Web Services Elasticache instance with PHP is quite simple. The following example code will demonstrate how to do so:

```
<?php

// Create a connection to the ElastiCache instance
$redis = new Redis();
$redis->connect('example.cache.amazonaws.com', 6379);

// Authenticate with the ElastiCache instance
$redis->auth('password');

// Set a value
$redis->set('key', 'value');

// Get the value
echo $redis->get('key');

?>
```

This example code will output the following:

```
value
```

The code is composed of the following parts:

1. `$redis = new Redis();` - This creates a new Redis object.
2. `$redis->connect('example.cache.amazonaws.com', 6379);` - This connects to the ElastiCache instance using the hostname and port provided.
3. `$redis->auth('password');` - This authenticates with the ElastiCache instance using the password provided.
4. `$redis->set('key', 'value');` - This sets a key/value pair in the ElastiCache instance.
5. `echo $redis->get('key');` - This retrieves the value from the ElastiCache instance.

For more information on connecting to an Amazon Web Services Elasticache instance with PHP, please refer to the following links:

- [Connecting to an ElastiCache Cluster with PHP](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/ConnectToCacheNode.html)
- [Redis PHP Extension](https://github.com/phpredis/phpredis)

onelinerhub: [How can I use PHP to connect to an Amazon Web Services Elasticache instance?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-connect-to-an-amazon-web-services-elasticache-instance)