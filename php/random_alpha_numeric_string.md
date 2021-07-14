# Generate random alpha-numeric string

```php
$random = bin2hex(random_bytes(32 / 2));

```

- $random - will contain final random string
- bin2hex - converts binary string into hex
- random_bytes - generates [random bytes](https://www.php.net/manual/function.random-bytes.php)
- 32 - length of the final random string

## Example
```php
echo bin2hex(random_bytes(32 / 2));
```
```bash
7c3d9491b35d84c8349b6874e4e10b33
```
