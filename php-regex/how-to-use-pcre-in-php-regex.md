# How to use PCRE in PHP regex?
// plain

PCRE stands for Perl Compatible Regular Expressions and is a library written in C that implements regular expression pattern matching using the same syntax and semantics as Perl 5. PCRE is used in PHP to provide a powerful and efficient way to perform regular expression matching.

## Example code

```
$pattern = '/^[a-zA-Z0-9_]{3,20}$/';
$string = 'my_username';

if (preg_match($pattern, $string)) {
    echo 'The string is valid!';
}
```

## Output example

```
The string is valid!
```

## Code explanation

- `$pattern`: This is the regular expression pattern that will be used to match the string. In this example, it is a pattern that matches strings that are 3 to 20 characters long and contain only letters, numbers, and underscores.
- `$string`: This is the string that will be tested against the regular expression pattern.
- `preg_match()`: This is the function used to match the string against the regular expression pattern. It takes two parameters: the regular expression pattern and the string to be tested.
- `echo`: This is the statement used to output the result of the regular expression match.

## Helpful links
- [PCRE Documentation](http://php.net/manual/en/ref.pcre.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PCRE in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-pcre-in-php-regex)