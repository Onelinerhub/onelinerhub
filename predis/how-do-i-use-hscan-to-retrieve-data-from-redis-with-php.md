# How do I use HSCAN to retrieve data from Redis with PHP?
// plain

Using HSCAN to retrieve data from Redis with PHP is very easy. First, you need to install the [predis/predis](https://github.com/nrk/predis) client library.

Then, you can use the `hscan` command to retrieve data from Redis. Here is an example:

```php
<?php

$client = new Predis\Client();

$cursor = 0;
do {
    // scan the hash
    $reply = $client->hscan('myhash', $cursor);

    // update the cursor
    $cursor = $reply->getCursor();

    // get the keys
    $keys = $reply->getKeys();

    // get the values
    $values = $reply->getValues();

    // do something with the keys and values

} while ($cursor != 0);
```

The code above will loop through the `myhash` hash and retrieve all of its keys and values. The output of the code above will be an array of keys and values.

## Code explanation


1. `$client = new Predis\Client();` - This line creates a new client object.
2. `$reply = $client->hscan('myhash', $cursor);` - This line uses the `hscan` command to retrieve data from the `myhash` hash.
3. `$cursor = $reply->getCursor();` - This line gets the next cursor position from the reply.
4. `$keys = $reply->getKeys();` - This line gets the keys from the reply.
5. `$values = $reply->getValues();` - This line gets the values from the reply.
6. `do something with the keys and values` - This line is where you can do something with the keys and values from the reply.

For more information, you can refer to the [Predis documentation](https://github.com/nrk/predis/wiki/Command-HSCAN).

onelinerhub: [How do I use HSCAN to retrieve data from Redis with PHP?](https://onelinerhub.com/predis/how-do-i-use-hscan-to-retrieve-data-from-redis-with-php)