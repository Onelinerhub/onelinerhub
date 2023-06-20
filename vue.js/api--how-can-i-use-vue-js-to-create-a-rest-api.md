# api

How can I use Vue.js to create a REST API?
// plain

Vue.js can be used to create a REST API by using the `vue-resource` library. This library allows you to make HTTP requests to external APIs and also handle responses. For example, you can use the `get` method to make a GET request to an external API and get the response data:

```
this.$http.get('http://example.com/api/data').then(response => {
  console.log(response.data);
});
```

The `response.data` variable will contain the response data from the external API.

## Code explanation


- `vue-resource` library: This library provides the methods to make HTTP requests to external APIs and handle responses.
- `get` method: This method is used to make a GET request to an external API.
- `response.data` variable: This variable contains the response data from the external API.

## Helpful links

- [vue-resource](https://github.com/pagekit/vue-resource)
- [Creating a RESTful API with Vue.js](https://blog.logrocket.com/creating-a-restful-api-with-vue-js-b2e3f6b4fe1b/)

onelinerhub: [api

How can I use Vue.js to create a REST API?](https://onelinerhub.com/vue.js/api--how-can-i-use-vue-js-to-create-a-rest-api)