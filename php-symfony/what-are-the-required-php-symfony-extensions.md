# What are the required PHP Symfony extensions?
// plain

The required PHP Symfony extensions are:

1. `intl`: This extension provides internationalization features like message translation, locale-specific date and time formatting, and number and currency formatting. Example code:
```
<?php
$formatter = new IntlDateFormatter('en_US', IntlDateFormatter::SHORT, IntlDateFormatter::SHORT);
echo $formatter->format(new DateTime());
```
## Output example
 `7/4/20`

2. `mbstring`: This extension provides multibyte string functions that help to manipulate multibyte characters. Example code:
```
<?php
echo mb_strlen('Hello World!');
```
## Output example
 `12`

3. `iconv`: This extension provides an interface to the iconv character set conversion facility. Example code:
```
<?php
echo iconv('UTF-8', 'ASCII//TRANSLIT', 'Hello World!');
```
## Output example
 `Hello World!`

4. `ctype`: This extension provides functions for character type checking and conversion. Example code:
```
<?php
echo ctype_alpha('Hello World!');
```
## Output example
 `false`

5. `tokenizer`: This extension provides a set of functions for tokenizing strings. Example code:
```
<?php
$tokens = token_get_all('<?php echo "Hello World!"; ?>');
print_r($tokens);
```
## Output example
 `Array ( [0] => Array ( [0] => 379 [1] => <?php echo "Hello World!"; ?> ) [1] => Array ( [0] => 307 [1] => echo ) [2] => Array ( [0] => 315 [1] => "Hello World!" ) [3] => Array ( [0] => 379 [1] => ; ) [4] => Array ( [0] => 379 [1] => ?> ) )`

## Helpful links

- [PHP: intl - Manual](https://www.php.net/manual/en/book.intl.php)
- [PHP: mbstring - Manual](https://www.php.net/manual/en/book.mbstring.php)
- [PHP: iconv - Manual](https://www.php.net/manual/en/book.iconv.php)
- [PHP: ctype - Manual](https://www.php.net/manual/en/book.ctype.php)
- [PHP: tokenizer - Manual](https://www.php.net/manual/en/book.tokenizer.php)

onelinerhub: [What are the required PHP Symfony extensions?](https://onelinerhub.com/php-symfony/what-are-the-required-php-symfony-extensions)