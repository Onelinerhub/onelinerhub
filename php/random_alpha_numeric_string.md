# Generate random alpha-numeric string

```php
$random = bin2hex(random_bytes(16 * 2)));

```

- $random - will contain final random string
- bin2hex - converts binary string into hex
- random_bytes - generates [random bytes](https://www.php.net/manual/function.random-bytes.php)
- 16 - length of the final random string
