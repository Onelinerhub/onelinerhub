# How to use PHP regex to match a word?
// plain

Using PHP regex to match a word is a powerful way to search for specific words or patterns in a string.

```
$string = "This is a string";

if (preg_match("/string/", $string)) {
    echo "Match found!";
}
```

## Output example
 `Match found!`

The code above uses the `preg_match()` function to search for the word "string" in the string `$string`. If the word is found, the `echo` statement will output "Match found!".

## Code explanation


- `preg_match()`: This is a PHP function used to search for a specific pattern in a string.
- `/string/`: This is the pattern we are searching for. It is enclosed in forward slashes.
- `$string`: This is the string we are searching in.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match a word?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-a-word)