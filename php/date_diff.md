# Find difference between two dates in days

```php
$days = (new DateTime($first))->diff( new DateTime($second) )->format('%a');
```

- $days - number of days between two dates will be returned here
- DateTime - system object to [manipulate dates/times](https://www.php.net/manual/class.datetime.php)
- $first - later date
- $second - earlier date
- '%a' - return number of days

# Example: 
```php
echo (new DateTime('2022-01-02'))->diff( new DateTime('2021-12-11') )->format('%a');
```
```bash
22
```
