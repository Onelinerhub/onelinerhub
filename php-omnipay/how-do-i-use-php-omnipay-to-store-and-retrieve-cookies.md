# How do I use PHP Omnipay to store and retrieve cookies?
// plain

PHP Omnipay provides a useful way to store and retrieve cookies. The following example code shows how to do this using the `setCookie()` and `getCookie()` functions.

```php
// Set a cookie
$cookieName = 'exampleCookie';
$cookieValue = 'exampleValue';
$cookieExpiry = time() + (60 * 60 * 24 * 7); // 7 day expiry
$omnipay->setCookie($cookieName, $cookieValue, $cookieExpiry);

// Retrieve a cookie
$cookieValue = $omnipay->getCookie($cookieName);
echo $cookieValue;
// Output: exampleValue
```

The code above sets a cookie named `exampleCookie` with value `exampleValue` and an expiry of 7 days. It then retrieves the cookie value and prints it to the screen.

## Code explanation


1. `$cookieName = 'exampleCookie';` - sets a variable `$cookieName` to a string `exampleCookie`
2. `$cookieValue = 'exampleValue';` - sets a variable `$cookieValue` to a string `exampleValue`
3. `$cookieExpiry = time() + (60 * 60 * 24 * 7);` - sets a variable `$cookieExpiry` to the current time plus 7 days
4. `$omnipay->setCookie($cookieName, $cookieValue, $cookieExpiry);` - sets a cookie with name `exampleCookie`, value `exampleValue` and expiry `$cookieExpiry`
5. `$cookieValue = $omnipay->getCookie($cookieName);` - retrieves the cookie value with name `exampleCookie`
6. `echo $cookieValue;` - prints the cookie value to the screen

## Helpful links

- [PHP Omnipay Documentation](https://omnipay.thephpleague.com/api/cookie-handling/)

onelinerhub: [How do I use PHP Omnipay to store and retrieve cookies?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-to-store-and-retrieve-cookies)