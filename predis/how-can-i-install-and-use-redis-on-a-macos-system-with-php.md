# How can I install and use Redis on a MacOS system with PHP?
// plain

To install and use Redis on a MacOS system with PHP, you can follow the steps below:

1. Install Homebrew (a package manager for MacOS) by running the command:
    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

2. Install Redis using Homebrew by running the command:
    ```
    brew install redis
    ```

3. Start Redis by running the command:
    ```
    brew services start redis
    ```

4. Install the PHP extension for Redis by running the command:
    ```
    pecl install redis
    ```

5. Enable the Redis extension in your `php.ini` file:
    ```
    extension=redis.so
    ```

6. Test the connection to Redis with a simple PHP script:
    ```php
    <?php
    $redis = new Redis();
    $redis->connect('127.0.0.1', 6379);
    echo "Connection to server sucessfully";
    // Check if server is running
    echo "Server is running: " . $redis->ping();
    ?>
    ```
    Output:
    ```
    Connection to server sucessfully
    Server is running: +PONG
    ```

7. You can now use Redis with your PHP scripts!

## Helpful links

- [Homebrew Documentation](https://brew.sh/index_pl)
- [Redis Documentation](https://redis.io/documentation)
- [PHP Redis extension](https://github.com/phpredis/phpredis)

onelinerhub: [How can I install and use Redis on a MacOS system with PHP?](https://onelinerhub.com/predis/how-can-i-install-and-use-redis-on-a-macos-system-with-php)