# How do I get query parameters using AngularJS?
// plain

Getting query parameters using AngularJS is quite easy. To do so, you can use the `$location` service. `$location` provides several methods to get query parameters. You can use `$location.search()` to get all the query parameters as a key-value object.

For example, if the URL is `http://example.com/?name=John&age=25`, then you can get the query parameters using:

```javascript
var queryParams = $location.search();
console.log(queryParams);
// Output: { name: 'John', age: '25' }
```

Here are the parts of the code and what they do:

- `var queryParams =`: This declares a variable to store the query parameters.
- `$location.search()`: This is a method of the `$location` service which returns an object containing the query parameters.
- `console.log(queryParams)`: This prints the query parameters to the console.

Here are some helpful links for further reading:

- [AngularJS $location](https://docs.angularjs.org/api/ng/service/$location)
- [Get query string parameter values using AngularJS](https://codepedia.info/get-query-string-parameter-values-using-angularjs/)

onelinerhub: [How do I get query parameters using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-get-query-parameters-using-angularjs)