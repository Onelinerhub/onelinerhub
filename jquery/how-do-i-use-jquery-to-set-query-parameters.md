# How do I use jQuery to set query parameters?
// plain

Using jQuery, query parameters can be set with the `.param()` method. This method takes one or more key/value pairs and returns a URL-encoded string.

## Example


```js
var params = {
    name: 'John',
    age: 30
};

var queryString = $.param(params);

console.log(queryString);
// Output: name=John&age=30
```

The `.param()` method takes two arguments:

1. An object containing key/value pairs that will be encoded into the query string.
2. An optional `traditional` boolean parameter that, when set to `true`, will use traditional (shallow) serialization.

The `.param()` method can also be used to retrieve the query string from a URL:

```js
var queryString = 'name=John&age=30';

var params = $.param(queryString);

console.log(params);
// Output: {name: 'John', age: '30'}
```

## Helpful links

- [jQuery.param() | jQuery API Documentation](https://api.jquery.com/jquery.param/)
- [jQuery.param() | jQuery Learning Center](https://learn.jquery.com/using-jquery-core/faq/how-do-i-get-querystring-values-in-jquery/)

onelinerhub: [How do I use jQuery to set query parameters?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-set-query-parameters)