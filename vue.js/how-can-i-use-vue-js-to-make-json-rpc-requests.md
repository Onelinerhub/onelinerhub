# How can I use Vue.js to make JSON-RPC requests?
// plain

Vue.js can be used to make JSON-RPC requests by using the Axios library. Axios is a promise-based HTTP client for making asynchronous HTTP requests. To make the request, the following code can be used:

```
import axios from 'axios'

const data = {
  jsonrpc: '2.0',
  method: 'sum',
  params: [1, 2, 4],
  id: 1
}

axios.post('http://example.com/api', data)
  .then(response => console.log(response))
  .catch(error => console.log(error))

// Output: {data: {jsonrpc: "2.0", result: 7, id: 1}}
```

1. `import axios from 'axios'` imports the Axios library.
2. `const data` creates a constant variable with the JSON-RPC request data.
3. `axios.post('http://example.com/api', data)` makes the request to the specified URL with the data.
4. `.then(response => console.log(response))` logs the response to the console.
5. `.catch(error => console.log(error))` logs any errors to the console.

## Helpful links

- [Axios documentation](https://github.com/axios/axios)
- [JSON-RPC documentation](https://www.jsonrpc.org/specification)

onelinerhub: [How can I use Vue.js to make JSON-RPC requests?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-make-json-rpc-requests)