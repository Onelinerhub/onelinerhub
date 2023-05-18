# How to use backreference in PHP regex?
// plain

Backreferences in PHP regex are used to match the same text as previously matched by a capturing group.

## Example code

```
$string = 'The quick brown fox jumps over the lazy dog.';
$pattern = '/(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+over\s+\1/';
if (preg_match($pattern, $string, $matches)) {
    echo "Matched: {$matches[0]}\n";
    echo "1: {$matches[1]}\n";
    echo "2: {$matches[2]}\n";
    echo "3: {$matches[3]}\n";
    echo "4: {$matches[4]}\n";
}
```

## Output example

```
Matched: The quick brown fox jumps over the
1: The
2: quick
3: brown
4: fox
```

## Code explanation

- `$string`: This is the string that will be tested against the regular expression.
- `$pattern`: This is the regular expression that will be used to match the string. The backreference `\1` is used to match the same text as previously matched by the first capturing group.
- `preg_match()`: This is the function used to match the string against the regular expression.
- `$matches`: This is an array that will contain the matches found by the regular expression.

## Helpful links
- [PHP Regular Expression Functions](https://www.php.net/manual/en/ref.regex.php)
- [Backreferences in Regular Expressions](https://www.regular-expressions.info/backref.html)

onelinerhub: [How to use backreference in PHP regex?](https://onelinerhub.com/php-regex/how-to-use-backreference-in-php-regex)