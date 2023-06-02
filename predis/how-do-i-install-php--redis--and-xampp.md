# How do I install PHP, Redis, and XAMPP?
// plain

1. **Installing PHP**
    - Download the latest version of PHP from the [official website](https://www.php.net/downloads.php).
    - Extract the downloaded file and place it in the desired location.
    - Add the path of the extracted folder to the `PATH` environment variable.
    - Open the command line and type `php -v` to verify the installation.

2. **Installing Redis**
    - Download the latest version of Redis from the [official website](https://redis.io/download).
    - Extract the downloaded file and place it in the desired location.
    - Open the command line and type `redis-server` to start the server.
    - Type `redis-cli ping` to verify the installation.

3. **Installing XAMPP**
    - Download the latest version of XAMPP from the [official website](https://www.apachefriends.org/index.html).
    - Run the downloaded installer and follow the instructions.
    - Open the command line and type `php -v` to verify the installation.

**Example Code**
```
// To verify PHP installation
php -v

// To start the Redis server
redis-server

// To verify Redis installation
redis-cli ping
```

**Output**
```
// To verify PHP installation
PHP 7.4.3 (cli) (built: Mar 26 2020 12:10:25) ( NTS Visual C++ 2017 x64 )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies

// To verify Redis installation
PONG
```

onelinerhub: [How do I install PHP, Redis, and XAMPP?](https://onelinerhub.com/predis/how-do-i-install-php--redis--and-xampp)