# How do I implement change detection in AngularJS?
// plain

Change detection in AngularJS is a feature that allows the framework to detect when a property of an object changes and take appropriate action.

To implement change detection in AngularJS, we must first use the `$watch` method on the scope of the controller. This method takes two parameters: the first is the expression to watch, and the second is the function to call when the expression changes.

For example:
```
$scope.$watch('name', function(newValue, oldValue) {
  console.log('Name changed from ' + oldValue + ' to ' + newValue);
});
```

In this example, the `$watch` method is used to detect when the `name` property of the scope changes. When it does, the function provided as the second parameter will be called, and the new and old values of the property will be passed as parameters.

The `$watch` method is the most basic way to implement change detection in AngularJS, but it can also be done using `$watchCollection` and `$watchGroup`.

* `$watchCollection`: monitors a collection of objects and calls the callback function when an item is added, removed, or changed.
* `$watchGroup`: monitors a collection of expressions and calls the callback function when any of the expressions change.

For more information on implementing change detection in AngularJS, see [this page](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$watch).

onelinerhub: [How do I implement change detection in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-implement-change-detection-in-angularjs)