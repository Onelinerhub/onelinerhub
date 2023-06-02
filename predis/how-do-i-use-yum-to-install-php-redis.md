# How do I use yum to install php-redis?
// plain

To use yum to install php-redis, you must first make sure that you have the appropriate repositories installed.

You can then use the following command:
```
sudo yum install php-redis
```
This will install the php-redis module and any other dependencies it requires.

Once the installation is complete, you can verify it by running the following command:
```
php -m | grep redis
```
This command should output something like the following:
```
redis
```

This indicates that the php-redis module is installed and ready to use.

Here is a breakdown of the code used:
* `sudo yum install php-redis` - This command is used to install the php-redis module.
* `php -m | grep redis` - This command is used to verify that the php-redis module is installed.

For more information, please refer to the following links:
* [Redis PHP Extension](https://redis.io/topics/redis-php)
* [Yum Command](https://linux.die.net/man/8/yum)

onelinerhub: [How do I use yum to install php-redis?](https://onelinerhub.com/predis/how-do-i-use-yum-to-install-php-redis)