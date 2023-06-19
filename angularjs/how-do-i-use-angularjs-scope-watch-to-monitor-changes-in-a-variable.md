# How do I use AngularJS scope watch to monitor changes in a variable?
// plain

AngularJS scope watch is used to monitor changes in a variable. It is a powerful tool that allows you to observe changes in the model and react accordingly.

```
$scope.$watch('variable', function (newVal, oldVal) {
    // Do something when the value changes
});
```

The above code will watch the variable for changes and execute the callback function when the value changes. The callback function will receive two parameters, newVal and oldVal, which are the new and old values of the variable respectively.

Below is an example of how to use scope watch to monitor changes in a variable:

```
$scope.myVar = 'Hello World';

$scope.$watch('myVar', function (newVal, oldVal) {
    console.log('myVar changed from ' + oldVal + ' to ' + newVal);
});
```

## Output example

```
myVar changed from Hello World to Hi World
```

The code above will watch the variable `myVar` for any changes and log a message to the console when the value changes.

## Helpful links
- [AngularJS Scope Watch](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$watch)
- [AngularJS Tutorial - Scope Watch](https://www.tutorialspoint.com/angularjs/angularjs_scope_watch.htm)

onelinerhub: [How do I use AngularJS scope watch to monitor changes in a variable?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-scope-watch-to-monitor-changes-in-a-variable)