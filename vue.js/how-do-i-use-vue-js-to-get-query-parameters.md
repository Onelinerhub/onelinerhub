# How do I use Vue.js to get query parameters?
// plain

Vue.js provides a simple way to access query parameters in the URL. To do this, you can use the `$route` object, which is available on all Vue components.

```javascript
// Get the query parameters
const queryParams = this.$route.query;
```

The `queryParams` object will contain all the query parameters in the URL. For example, if the URL is `http://example.com?name=John&age=20`, the `queryParams` object will look like this:

```javascript
{
    name: "John",
    age: 20
}
```

You can also use the `$route` object to get the full URL, including the query parameters:

```javascript
// Get the full URL
const fullUrl = this.$route.fullPath;

// Outputs: http://example.com?name=John&age=20
console.log(fullUrl);
```

To learn more about the `$route` object, please refer to the [Vue.js documentation](https://vuejs.org/v2/api/#route).

onelinerhub: [How do I use Vue.js to get query parameters?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-to-get-query-parameters)