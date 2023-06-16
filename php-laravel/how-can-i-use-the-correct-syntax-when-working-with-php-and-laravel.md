# How can I use the correct syntax when working with PHP and Laravel?
// plain

Using the correct syntax when working with PHP and Laravel is essential for the stability and security of your code. Here are some tips for writing code correctly:

1. Use strict types for variables. For example:

```
<?php
declare(strict_types=1);
$num = 5;
echo $num;
```

## Output example

```
5
```

2. Use type casting when necessary. For example:

```
<?php
$num = "5";
$intNum = (int) $num;
echo $intNum;
```

## Output example

```
5
```

3. Use the correct syntax for loops. For example:

```
<?php
for ($i = 0; $i < 5; $i++) {
    echo $i;
}
```

## Output example

```
01234
```

4. Use the correct syntax for if statements. For example:

```
<?php
$num = 5;
if ($num == 5) {
    echo "Number is 5";
}
```

## Output example

```
Number is 5
```

5. Use the correct syntax for functions. For example:

```
<?php
function sayHello($name) {
    echo "Hello, " . $name;
}

sayHello("John");
```

## Output example

```
Hello, John
```

For more information, please refer to the following links:

- [PHP Syntax](https://www.w3schools.com/php/php_syntax.asp)
- [Laravel Syntax](https://laravel.com/docs/7.x/blade#blade-syntax)
- [PHP Type Casting](https://www.w3schools.com/php/php_type_casting.asp)

onelinerhub: [How can I use the correct syntax when working with PHP and Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-the-correct-syntax-when-working-with-php-and-laravel)