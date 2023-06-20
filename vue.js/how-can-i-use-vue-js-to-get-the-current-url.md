# How can I use Vue.js to get the current URL?
// plain

Using Vue.js to get the current URL is easy. You can use the `$route` object from the `vue-router` plugin. The `$route.path` property will give you the current URL.

## Example code

```javascript
console.log(this.$route.path);
```
## Output example

```
/current/url
```

The code above will output the current URL. Here is a breakdown of the code:
- `console.log`: prints the given parameter to the console
- `this.$route`: the `$route` object from the `vue-router` plugin
- `$route.path`: the property of the `$route` object that contains the current URL

For more information, you can check out the [Vue.js documentation](https://vuejs.org/v2/api/#vue-router) and the [vue-router documentation](https://router.vuejs.org/api/#route-object).

onelinerhub: [How can I use Vue.js to get the current URL?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-get-the-current-url)