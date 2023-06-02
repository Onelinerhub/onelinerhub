# How can I use Redis to search for data stored in a PHP application?
// plain

Redis can be used to search for data stored in a PHP application by using the `KEYS` command. This command takes a pattern as an argument and returns all the keys that match the pattern. For example:

```
127.0.0.1:6379> KEYS user:*
1) "user:1"
2) "user:2"
3) "user:3"
```

The `KEYS` command is powerful and can be used to search for any type of data stored in Redis. It can also be used to search for data stored in a PHP application. For example, if you have stored user information in a Redis hash, you can use the `HKEYS` command to search for user information.

```
127.0.0.1:6379> HKEYS user:1
1) "name"
2) "age"
3) "email"
```

You can also use the `SORT` command to sort data stored in a PHP application. For example, you can sort a list of user IDs by age:

```
127.0.0.1:6379> SORT user:* BY age
1) "user:3"
2) "user:1"
3) "user:2"
```

These are just a few examples of how Redis can be used to search for data stored in a PHP application. For more information, please see the [Redis documentation](https://redis.io/commands).

onelinerhub: [How can I use Redis to search for data stored in a PHP application?](https://onelinerhub.com/predis/how-can-i-use-redis-to-search-for-data-stored-in-a-php-application)