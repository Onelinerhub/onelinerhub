# How can I install and configure Redis on an Ubuntu server running PHP?
// plain

1. Install Redis on Ubuntu server:
   ```
   sudo apt-get install redis-server
   ```
   This will install Redis server on the server.

2. Configure Redis:
   Edit the Redis configuration file `/etc/redis/redis.conf` and set the `bind` directive to the IP address of the server.

3. Start Redis:
   ```
   sudo service redis-server start
   ```
   This will start the Redis server.

4. Test Redis:
   ```
   redis-cli ping
   ```
   Output:
   ```
   PONG
   ```

5. Install PHP Redis extension:
   ```
   sudo apt-get install php-redis
   ```
   This will install the Redis extension for PHP.

6. Configure PHP Redis extension:
   Edit the `php.ini` file and add the line `extension=redis.so`.

7. Restart Apache:
   ```
   sudo service apache2 restart
   ```
   This will restart Apache and enable the Redis extension.

## Helpful links
- [Redis Quickstart](https://redis.io/topics/quickstart)
- [PHP Redis Documentation](https://redis.io/clients/php)

onelinerhub: [How can I install and configure Redis on an Ubuntu server running PHP?](https://onelinerhub.com/predis/how-can-i-install-and-configure-redis-on-an-ubuntu-server-running-php)