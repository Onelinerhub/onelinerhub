# How can I use query params in Vue.js?
// plain

Query params are a great way to pass data between routes in a Vue.js application. To use query params, you can use the `$route` object to access the query params in the current route.

For example, if the URL is `http://localhost:8080/route?param1=value1&param2=value2`, you can access the query params like this:

```javascript
const param1 = this.$route.query.param1;
const param2 = this.$route.query.param2;

console.log(param1); // value1
console.log(param2); // value2
```

You can also use the `$router` object to set query params. For example, to set `param3` to `value3`:

```javascript
this.$router.push({ query: { param3: 'value3' } });
```

This will change the URL to `http://localhost:8080/route?param1=value1&param2=value2&param3=value3`.

## Code explanation


1. `this.$route.query.param1`: accesses the `param1` query parameter in the current route.
2. `this.$router.push({ query: { param3: 'value3' } });`: sets the `param3` query parameter to `value3`.

## Helpful links

- [Vue Router docs](https://router.vuejs.org/guide/)
- [Vue.js docs](https://vuejs.org/v2/guide/)

onelinerhub: [How can I use query params in Vue.js?](https://onelinerhub.com/vue.js/how-can-i-use-query-params-in-vue-js)