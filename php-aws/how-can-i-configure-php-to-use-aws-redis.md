# How can I configure PHP to use AWS Redis?
// plain

To configure PHP to use AWS Redis, follow the steps below:

1. Install the AWS SDK for PHP. This can be done using Composer with the command:
```
composer require aws/aws-sdk-php
```

2. Create a Redis client object. This requires the endpoint of the AWS ElastiCache Redis cluster and credentials for an IAM user with access to the cluster.

```
$redisClient = new Aws\ElastiCache\ElastiCacheClient([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => 'IAM_USER_KEY',
        'secret' => 'IAM_USER_SECRET',
    ],
]);
```

3. Use the Redis client object to connect to the cluster.

```
$redis = $redisClient->getConnection([
    'Endpoint' => [
        'Address' => 'redis-cluster-endpoint',
        'Port'    => 6379,
    ],
]);
```

4. Use the Redis connection object to execute commands.

```
$redis->set('key', 'value');
```

5. Disconnect from the cluster when finished.

```
$redis->disconnect();
```

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [AWS ElastiCache Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.ElastiCache.ElastiCacheClient.html)

onelinerhub: [How can I configure PHP to use AWS Redis?](https://onelinerhub.com/php-aws/how-can-i-configure-php-to-use-aws-redis)