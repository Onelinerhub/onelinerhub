# How do I fix the "fetch is not defined" error when using Express.js?
// plain

The "fetch is not defined" error occurs when you try to use the `fetch` API in Express.js. To fix this error, you need to make sure that the `fetch` API is imported into your Express.js project.

For example, you can use the `node-fetch` package by adding the following code to your project:

```
const fetch = require('node-fetch');
```

Once `node-fetch` is imported, you can use the `fetch` API in your Express.js project:

```
fetch('https://example.com/api')
  .then(res => res.json())
  .then(json => console.log(json))
```

## Output example

```
{
  "data": {
    "name": "John Doe"
  }
}
```

The code above will import the `node-fetch` package and use the `fetch` API to make a request to `https://example.com/api` and print the response in the console.

If you are using `fetch` for the first time, you can find out more about it [here](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

You can also find out more about the `node-fetch` package [here](https://www.npmjs.com/package/node-fetch).

onelinerhub: [How do I fix the "fetch is not defined" error when using Express.js?](https://onelinerhub.com/expressjs/how-do-i-fix-the--fetch-is-not-defined--error-when-using-express-js)