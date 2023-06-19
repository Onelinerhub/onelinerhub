# How do I use AngularJS to get a cookie?
// plain

To use AngularJS to get a cookie, use the `$cookies` service. This service provides a key-value based API for reading and writing cookies.

## Example code

```
// Get a cookie
var cookie = $cookies.get('cookieName');
console.log(cookie);
```
## Output example

```
cookieValue
```

The code above uses the `$cookies.get()` method to get a cookie with the name `cookieName` and stores the value in the `cookie` variable. The value of the cookie is then logged to the console.

The `$cookies` service also provides the following methods:
* `$cookies.put(key, value)`: sets a cookie with the given key and value
* `$cookies.remove(key)`: removes a cookie with the given key
* `$cookies.getObject(key)`: gets an object from a cookie with the given key
* `$cookies.putObject(key, value)`: sets an object in a cookie with the given key and value

For more information, see the [AngularJS $cookies service documentation](https://docs.angularjs.org/api/ngCookies/service/$cookies).

onelinerhub: [How do I use AngularJS to get a cookie?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-get-a-cookie)