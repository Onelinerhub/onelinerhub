# How can I fix the issue of PHP startup unable to initialize Redis module?
// plain

1. First, check if the Redis module is installed on the system. To do this, run the command `php -m` in the terminal and look for the `redis` module in the output.

2. If the `redis` module is not present in the output, it needs to be installed. To install the `redis` module, run the command `sudo pecl install redis`.

3. After the `redis` module is installed, add the line `extension=redis.so` to the `php.ini` file.

4. Restart the web server for the changes to take effect.

5. Once the web server is restarted, run the command `php -m` again to check if the `redis` module is present in the output.

6. If the `redis` module is present, then the issue of PHP startup unable to initialize Redis module should be fixed.

7. If the issue is still not fixed, then it is recommended to check the [Redis documentation](https://redis.io/topics/quickstart) for more information.

onelinerhub: [How can I fix the issue of PHP startup unable to initialize Redis module?](https://onelinerhub.com/predis/how-can-i-fix-the-issue-of-php-startup-unable-to-initialize-redis-module)