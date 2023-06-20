# How can I use Vue.js to make an Ajax call?
// plain

Vue.js provides an easy way to make an Ajax call using the `axios` library. `axios` is a promise based HTTP client for the browser and node.js.

## Example code

```javascript
axios.get('/user?ID=12345')
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
```
## Output example

```javascript
{data: {…}, status: 200, statusText: "OK", headers: {…}, config: {…}, …}
```

## Code explanation

- `axios.get`: Makes a `GET` request to the specified URL.
- `/user?ID=12345`: The URL to make the request to.
- `then`: Executes the callback function if the request is successful.
- `catch`: Executes the callback function if the request fails.

## Helpful links
- [Axios Documentation](https://github.com/axios/axios)
- [Vue.js Guide](https://vuejs.org/v2/guide/)

onelinerhub: [How can I use Vue.js to make an Ajax call?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-make-an-ajax-call)