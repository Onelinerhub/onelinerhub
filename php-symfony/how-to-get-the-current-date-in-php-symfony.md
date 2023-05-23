# How to get the current date in PHP Symfony?
// plain

The current date can be obtained in PHP Symfony using the DateTime class.

## Example code

```
$date = new \DateTime();
echo $date->format('Y-m-d H:i:s');
```

## Output example

```
2020-09-17 11:45:00
```

## Code explanation

- `$date = new \DateTime();`: creates a new DateTime object
- `echo $date->format('Y-m-d H:i:s');`: formats the date object to the desired format

## Helpful links
- [PHP DateTime class](https://www.php.net/manual/en/class.datetime.php)
- [PHP DateTime format](https://www.php.net/manual/en/datetime.format.php)

onelinerhub: [How to get the current date in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-get-the-current-date-in-php-symfony)