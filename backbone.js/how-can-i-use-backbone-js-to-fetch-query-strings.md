# How can I use Backbone.js to fetch query strings?
// plain

Backbone.js provides a convenient way to fetch query strings from the URL. To do this, you will need to use the `Backbone.history.getFragment()` method. This method will return a string containing the query string parameters.

For example, given a URL of `http://example.com?query=example`, the following code would return `query=example`:

```javascript
let queryString = Backbone.history.getFragment();
console.log(queryString);

// Output: query=example
```

The code works by:

1. Declaring a variable, `queryString`, and assigning it the value returned by the `Backbone.history.getFragment()` method.
2. Logging the value of `queryString` to the console.

For more information, please see the [Backbone.js documentation](http://backbonejs.org/#History).

onelinerhub: [How can I use Backbone.js to fetch query strings?](https://onelinerhub.com/backbone.js/how-can-i-use-backbone-js-to-fetch-query-strings)