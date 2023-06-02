# How do I install PHP Redis on Ubuntu 20.04?
// plain

1. Install the Redis server using the apt command:
```
sudo apt install redis-server
```
2. Once the installation is complete, you can start the Redis server using the systemctl command:
```
sudo systemctl start redis-server
```
3. Now, you can install the PHP Redis extension with the following command:
```
sudo apt install php-redis
```
4. After the installation is complete, you can enable the extension by editing the php.ini file.
```
sudo nano /etc/php/7.4/apache2/php.ini
```
5. Add the following line to the php.ini file to enable the Redis extension:
```
extension=redis.so
```
6. Finally, restart the Apache web server to apply the changes.
```
sudo systemctl restart apache2
```
7. To test the installation, create a PHP file with the following code:
```
<?php
$redis = new Redis();
if ($redis->connect('127.0.0.1', 6379)) {
    echo "Connection to server sucessfully";
} else {
    echo "Connection to server failed";
}
?>
```
The output should be:
```
Connection to server sucessfully
```

## Helpful links

- [Redis Quick Start](https://redis.io/topics/quickstart)
- [How To Install and Use Redis on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis-on-ubuntu-20-04)

onelinerhub: [How do I install PHP Redis on Ubuntu 20.04?](https://onelinerhub.com/predis/how-do-i-install-php-redis-on-ubuntu------)