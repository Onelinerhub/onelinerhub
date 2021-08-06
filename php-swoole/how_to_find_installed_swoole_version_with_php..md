# How to find installed Swoole version with PHP.

```php
php -i | grep swoole -1 | grep Version
```

- php -i - shows PHP system information
- grep Version - filters out line with PHP Swoole version
