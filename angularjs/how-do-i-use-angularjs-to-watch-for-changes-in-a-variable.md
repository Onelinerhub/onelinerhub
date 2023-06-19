# How do I use AngularJS to watch for changes in a variable?
// plain

AngularJS provides a `$watch` function that can be used to watch for changes in a variable. To use it, you can inject the `$scope` service into your controller and then call the `$watch` function, passing in the variable name you want to watch.

For example, if you want to watch for changes in a variable called `name`, you can do the following:

```javascript
$scope.$watch('name', function(newValue, oldValue) {
  console.log('name changed from ' + oldValue + ' to ' + newValue);
});
```

The `$watch` function takes two arguments:

1. The variable name (in this case `name`).
2. A callback function that will be called when the variable changes. This callback function will be passed two arguments: the new value of the variable, and the old value of the variable.

In this example, when `name` changes, the callback function will log the change to the console.

For more information on the `$watch` function, see the [AngularJS Documentation](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$watch).

onelinerhub: [How do I use AngularJS to watch for changes in a variable?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-watch-for-changes-in-a-variable)