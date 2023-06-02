# How to configure the PHP Redis extension in XAMPP?
// plain

The PHP Redis extension can be configured in XAMPP by following these steps:

1. Download the [PHP Redis extension](https://pecl.php.net/package/redis) from the PECL website and unzip it into the `C:\xampp\php\ext` folder.

2. Open the `php.ini` file located in the `C:\xampp\php` folder and add the following line to the end of the file:

```
extension=php_redis.dll
```

3. Restart the Apache server in the XAMPP control panel.

4. Open the `C:\xampp\php\ext\php_redis.dll` file in a text editor and change the following line of code:

```
#define PHP_REDIS_VERSION "4.2.0"
```

to

```
#define PHP_REDIS_VERSION "5.2.0"
```

5. Save the `php_redis.dll` file and restart the Apache server again.

6. To verify that the PHP Redis extension is installed correctly, create a new file called `test.php` in the `C:\xampp\htdocs` folder and add the following code to it:

```
<?php

if (function_exists('redis')) {
    echo "PHP Redis extension is installed.";
} else {
    echo "PHP Redis extension is not installed.";
}

?>
```

7. Open `http://localhost/test.php` in your browser and you should see the output `PHP Redis extension is installed.`

**Output:**

`PHP Redis extension is installed.`

onelinerhub: [How to configure the PHP Redis extension in XAMPP?](https://onelinerhub.com/predis/how-to-configure-the-php-redis-extension-in-xampp)