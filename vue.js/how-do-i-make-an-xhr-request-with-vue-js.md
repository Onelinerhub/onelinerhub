# How do I make an XHR request with Vue.js?
// plain

To make an XHR request with Vue.js, you can use the [`axios`](https://github.com/axios/axios) library. `axios` is an easy to use library that provides a simple API for making HTTP requests from the browser and Node.js.

Here is an example of an XHR request with `axios`:

```javascript
axios.get('/user?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });
```

If the request is successful, the `response` object will contain the response data. If the request fails, the `error` object will contain information about the error that occurred.

You can also pass in additional options to customize the request. For example, you can set the `headers` option to pass in custom headers:

```javascript
axios.get('/user?ID=12345', {
  headers: {
    'X-Custom-Header': 'foobar'
  }
})
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });
```

You can learn more about `axios` and XHR requests in the [Vue.js documentation](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html).

onelinerhub: [How do I make an XHR request with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-make-an-xhr-request-with-vue-js)