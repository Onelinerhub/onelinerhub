# Get Command Line Input Mid-Runtime

### Use ``readline`` to take input:

```php
echo "Enter a number:\n";
$input = readline('> ');
echo "Entered: " . $input;
```

- ``echo "Enter a number\n";`` - give the user a prompt
- ``$input =`` - assign the input to the variable ``$input``
- ``readline(`` - reads what the user enters
- ``'> '`` - a stylistic prompt (purely aesthetic)
- ``echo $input;`` output what the user entered

## Example:
```
Enter a number:
> 10
Entered: 10
```
