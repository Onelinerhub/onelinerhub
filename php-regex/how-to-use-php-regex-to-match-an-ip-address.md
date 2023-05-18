# How to use PHP regex to match an IP address?
// plain

To match an IP address using PHP regex, you can use the following code:
```
$ip = '127.0.0.1';
if (preg_match('/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/', $ip)) {
    echo 'IP address is valid';
} else {
    echo 'IP address is not valid';
}
```
## Output example

```
IP address is valid
```

The code consists of the following parts:

1. `$ip = '127.0.0.1';` - This is the IP address that we are trying to match.

2. `preg_match('/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/', $ip)` - This is the regular expression used to match the IP address. It consists of two parts:
    - `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}` - This part matches the first three octets of the IP address. It consists of three parts:
        - `[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]` - This part matches a single octet of the IP address. It consists of five parts:
            - `[0-9]` - This part matches any number between 0 and 9.
            - `[1-9][0-9]` - This part matches any number between 10 and 99.
            - `1[0-9]{2}` - This part matches any number between 100 and 199.
            - `2[0-4][0-9]` - This part matches any number between 200 and 249.
            - `25[0-5]` - This part matches any number between 250 and 255.
        - `\` - This is an escape character.
        - `\.` - This part matches a single dot.
    - `([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$` - This part matches the fourth octet of the IP address. It is the same as the first part.

3. `if (preg_match('/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/', $ip)) {` - This is an if statement that checks if the IP address matches the regular expression.

4. `echo 'IP address is valid';` - This is the code that is executed if the IP address matches the regular expression.

5. `echo 'IP address is not valid';` - This is the code that is executed if the IP address does not match the regular expression.

## Helpful links
- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expression Syntax](https://www.regular-expressions.info/refquick.html)

onelinerhub: [How to use PHP regex to match an IP address?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-an-ip-address)