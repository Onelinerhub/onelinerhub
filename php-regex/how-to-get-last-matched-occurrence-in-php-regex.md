# How to get last matched occurrence in PHP regex?
// plain

The `preg_match_all` function in PHP can be used to get the last matched occurrence in a regular expression. This function takes three parameters: the pattern, the subject string, and an array to store the matches. The fourth parameter can be used to specify the flags, such as `PREG_OFFSET_CAPTURE` which will capture the offset of the last matched occurrence.

```php
$subject = 'This is a test string';
$pattern = '/\w+/';

preg_match_all($pattern, $subject, $matches, PREG_OFFSET_CAPTURE);

echo $matches[0][count($matches[0])-1][0]; // Output: string
```

The code above will capture all the matches of the pattern `/\w+/` in the subject string `This is a test string`. The `PREG_OFFSET_CAPTURE` flag will capture the offset of each match. The last matched occurrence can then be accessed by using the `count($matches[0])-1` index of the `$matches` array.

- `$subject`: The subject string to be matched against the pattern.
- `$pattern`: The regular expression pattern.
- `$matches`: An array to store the matches.
- `PREG_OFFSET_CAPTURE`: A flag to capture the offset of each match.
- `count($matches[0])-1`: The index of the last matched occurrence.

## Helpful links
- [PHP preg_match_all](https://www.php.net/manual/en/function.preg-match-all.php)
- [PHP preg_match](https://www.php.net/manual/en/function.preg-match.php)

onelinerhub: [How to get last matched occurrence in PHP regex?](https://onelinerhub.com/php-regex/how-to-get-last-matched-occurrence-in-php-regex)