# How do I set a cookie using Express.js?
// plain

Using Express.js, you can set a cookie with the `res.cookie()` method. This method takes two parameters: the name of the cookie and an object containing the options for that cookie.

## Example code

```
res.cookie('name', 'value', {
    maxAge: 1000 * 60 * 60 * 24 * 7, // 7 days
    httpOnly: true,
    sameSite: 'Strict'
});
```

This code will set a cookie named `name` with the value `value` that will expire in 7 days, is only available over HTTP, and is set with the `Strict` sameSite option.

## Code explanation

- `res.cookie('name', 'value', {` - this is the method that sets the cookie, with the name and value of the cookie as the first two parameters
- `maxAge: 1000 * 60 * 60 * 24 * 7` - this is the option that sets the cookie to expire in 7 days
- `httpOnly: true` - this option sets the cookie to only be available over HTTP
- `sameSite: 'Strict'` - this option sets the cookie with the `Strict` sameSite option

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html#res.cookie)
- [MDN Web Docs - HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

onelinerhub: [How do I set a cookie using Express.js?](https://onelinerhub.com/expressjs/how-do-i-set-a-cookie-using-express-js)