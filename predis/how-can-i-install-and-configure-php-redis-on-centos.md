# How can I install and configure php-redis on CentOS?
// plain

1. Install Redis server on CentOS. The installation process is very simple, just execute the following command:
```
sudo yum install redis
```

2. Start the Redis service and enable it to start at boot:
```
sudo systemctl start redis
sudo systemctl enable redis
```

3. Install php-redis extension. Execute the following command to install the extension:
```
sudo yum install php-pecl-redis
```

4. Configure php-redis extension. Open the php.ini configuration file and add the following line:
```
extension=redis.so
```

5. Restart the Apache service for the changes to take effect:
```
sudo systemctl restart httpd
```

6. Test the installation. Create a file called test.php in the web root directory and add the following code:
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

7. Open the test.php file in the browser. You should see the following output:
```
Connection to server sucessfully
```

**## Helpful links**

- [Install Redis on CentOS 7](https://linuxize.com/post/how-to-install-and-configure-redis-on-centos-7/)
- [Install php-pecl-redis on CentOS 7](https://www.tecmint.com/install-php-redis-extension-on-centos-7/)

onelinerhub: [How can I install and configure php-redis on CentOS?](https://onelinerhub.com/predis/how-can-i-install-and-configure-php-redis-on-centos)