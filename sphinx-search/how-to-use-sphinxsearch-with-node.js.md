# How to use SphinxSearch with Node.js?
// plain

SphinxSearch is a full-text search engine written in C++. It can be used with Node.js through the [node-sphinxclient](https://github.com/baryshev/node-sphinxclient) module.

To use SphinxSearch with Node.js, first install the node-sphinxclient module:

```
npm install sphinxclient
```

Then, create a new instance of the SphinxClient class:

```
var sphinx = new SphinxClient();
```

Finally, use the `query()` method to execute a search query:

```
sphinx.query('search query', function(err, result) {
  if (err) throw err;
  console.log(result);
});
```

The `query()` method takes two parameters: a search query string and a callback function. The callback function will be called with two parameters: an error object and a result object. The result object contains the search results.

## Code explanation


1. `npm install sphinxclient` - Installs the node-sphinxclient module.
2. `var sphinx = new SphinxClient();` - Creates a new instance of the SphinxClient class.
3. `sphinx.query('search query', function(err, result) { ... });` - Executes a search query and calls the callback function with two parameters: an error object and a result object.

## Helpful links

- [node-sphinxclient](https://github.com/baryshev/node-sphinxclient) - Node.js module for using SphinxSearch.

onelinerhub: [How to use SphinxSearch with Node.js?](https://onelinerhub.com/sphinx-search/how-to-use-sphinxsearch-with-node.js)