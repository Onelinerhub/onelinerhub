# How can I use Lodash to convert a JavaScript object to a query string?
// plain

Using Lodash, you can convert a JavaScript object to a query string with the `_.toQueryString()` method.

For example, given the following object:

```
let params = {
  name: 'John',
  age: 30
};
```

You can convert it to a query string with the following code:

```
let queryString = _.toQueryString(params);
console.log(queryString);
```

## Output example


```
name=John&age=30
```

The code consists of the following parts:

1. `let params = { name: 'John', age: 30 };` - declaring an object with two properties.
2. `let queryString = _.toQueryString(params);` - using the `_.toQueryString()` method to convert the object into a query string.
3. `console.log(queryString);` - logging the query string to the console.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs)
- [toQueryString() Documentation](https://lodash.com/docs/4.17.15#toQueryString)

onelinerhub: [How can I use Lodash to convert a JavaScript object to a query string?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-convert-a-javascript-object-to-a-query-string)