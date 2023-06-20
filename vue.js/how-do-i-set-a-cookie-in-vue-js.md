# How do I set a cookie in Vue.js?
// plain

To set a cookie in Vue.js, you can use the `Vue.cookie` library. The library provides an API for setting, getting and deleting cookies.

## Example code

```js
// Set a cookie
Vue.cookie.set('myCookie', 'value', { expires: '1Y' })

// Get a cookie
let myCookie = Vue.cookie.get('myCookie')

// Delete a cookie
Vue.cookie.delete('myCookie')
```

The code above sets a cookie named `myCookie` with value `value` that expires in one year. It then retrieves the cookie value and deletes the cookie.

Parts of the code:
- `Vue.cookie.set(name, value, options)`: Sets a cookie with the given name and value. The `options` parameter is an object that can contain additional options such as `expires`, `path`, `domain`, `secure` and `sameSite`.
- `Vue.cookie.get(name)`: Retrieves the value of a cookie with the given name.
- `Vue.cookie.delete(name)`: Deletes a cookie with the given name.

## Helpful links
- [Vue.cookie documentation](https://github.com/alfhen/vue-cookie#readme)
- [MDN Web Docs - Document.cookie](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)

onelinerhub: [How do I set a cookie in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-set-a-cookie-in-vue-js)