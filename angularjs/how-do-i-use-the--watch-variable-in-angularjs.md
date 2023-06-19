# How do I use the $watch variable in AngularJS?
// plain

The $watch variable in AngularJS is used to watch for changes in a variable or an expression. It is a function that is called whenever the value of the expression changes.

For example, the following code block will watch for changes in the variable `myVar` and log the new value when it changes:

```
$scope.$watch('myVar', function(newValue, oldValue) {
  console.log(newValue);
});
```

The `$watch` function takes two parameters: the expression to watch and the callback function to be called when the value of the expression changes. The callback function takes two parameters: the new value and the old value of the expression.

The `$watch` function returns a deregistration function that can be used to unregister the watch. This is useful when the watch is no longer needed.

Here is an example of using the deregistration function:

```
var deregistrationFn = $scope.$watch('myVar', function(newValue, oldValue) {
  console.log(newValue);
});

// Later on when the watch is no longer needed
deregistrationFn();
```

## Helpful links

- [AngularJS $watch Documentation](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$watch)
- [AngularJS $watch Tutorial](https://www.tutorialspoint.com/angularjs/angularjs_scope_watch.htm)

onelinerhub: [How do I use the $watch variable in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the--watch-variable-in-angularjs)