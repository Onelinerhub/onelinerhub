# How to install Redis on Red Hat 8 using PHP?
// plain

1. Install the **Redis** package from the Red Hat 8 repository:
```
sudo dnf install redis
```
2. Start the **Redis** service:
```
sudo systemctl start redis
```
3. Check the status of the **Redis** service:
```
sudo systemctl status redis
```
## Output example

```
● redis.service - Redis persistent key-value database
   Loaded: loaded (/usr/lib/systemd/system/redis.service; enabled; vendor preset: disabled)
   Active: active (running) since Thu 2020-07-09 11:30:50 UTC; 1min ago
 Main PID: 2989 (redis-server)
    Tasks: 4 (limit: 1186)
   Memory: 4.2M
   CGroup: /system.slice/redis.service
           └─2989 /usr/bin/redis-server 127.0.0.1:6379
```
4. Configure the **Redis** service to start automatically when the system boots:
```
sudo systemctl enable redis
```
5. Install the **PHP Redis** extension:
```
sudo dnf install php-pecl-redis
```
6. Restart the **Apache** web server to make the **PHP Redis** extension available:
```
sudo systemctl restart httpd
```
7. Verify the installation of the **PHP Redis** extension:
```
php -m | grep redis
```
## Output example

```
redis
```

## Helpful links
- [Red Hat 8 Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/)
- [Redis Documentation](https://redis.io/documentation)
- [PHP Redis Extension](https://pecl.php.net/package/redis)

onelinerhub: [How to install Redis on Red Hat 8 using PHP?](https://onelinerhub.com/predis/how-to-install-redis-on-red-hat---using-php)