# How do I store and retrieve cookies in Vue.js?
// plain

Storing and retrieving cookies in Vue.js is easy to do with the [vue-cookies](https://www.npmjs.com/package/vue-cookies) package.

First, install the package with `npm install vue-cookies --save`.

Then, import the package in the main.js file of your Vue.js project:

```js
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)
```

Once imported, you can set and retrieve cookies like this:

```js
// Set a cookie
this.$cookies.set('name', 'John Doe')

// Retrieve a cookie
let name = this.$cookies.get('name')

// Output: John Doe
console.log(name)
```

You can also set cookie options such as expiration date and domain:

```js
this.$cookies.set('name', 'John Doe', '2h')
```

The above will set the cookie to expire in 2 hours.

You can also delete a cookie like this:

```js
this.$cookies.remove('name')
```

This will delete the cookie with the key `name`.

onelinerhub: [How do I store and retrieve cookies in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-store-and-retrieve-cookies-in-vue-js)