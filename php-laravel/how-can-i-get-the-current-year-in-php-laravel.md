# How can I get the current year in PHP Laravel?
// plain

To get the current year in PHP Laravel, you can use the `\Carbon\Carbon::now()->year` method. This method will return the current year as an integer value.

## Example code

```
$year = \Carbon\Carbon::now()->year;
echo $year;
```

## Output example

```
2020
```

The code above includes the following parts:
* `\Carbon\Carbon::now()`: This is a Carbon class method that returns an instance of the Carbon class.
* `->year`: This is a Carbon class method that returns the current year as an integer.

## Helpful links
* [Carbon Documentation](https://carbon.nesbot.com/docs/)

onelinerhub: [How can I get the current year in PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-get-the-current-year-in-php-laravel)