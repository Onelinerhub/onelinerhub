# How can I use query parameters in an AngularJS application?
// plain

Query parameters are an important part of an AngularJS application and can be used to pass extra data to a page or component. Here is an example of how to use query parameters in an AngularJS application:

```
// Get the query parameters
var params = $location.search();

// Get a specific query parameter
var param1 = params.param1;

// Set a query parameter
$location.search('param1', 'value1');
```

The `$location.search()` method is used to get the query parameters from the URL, and the `$location.search('param1', 'value1')` method is used to set a query parameter.

## Code explanation


- `$location.search()` - This is used to get the query parameters from the URL.
- `params.param1` - This is used to get a specific query parameter from the URL.
- `$location.search('param1', 'value1')` - This is used to set a query parameter.

## Helpful links

- [AngularJS $location Service](https://docs.angularjs.org/api/ng/service/$location)
- [AngularJS Query Parameters](https://www.tutorialspoint.com/angularjs/angularjs_query_parameters.htm)

onelinerhub: [How can I use query parameters in an AngularJS application?](https://onelinerhub.com/angularjs/how-can-i-use-query-parameters-in-an-angularjs-application)