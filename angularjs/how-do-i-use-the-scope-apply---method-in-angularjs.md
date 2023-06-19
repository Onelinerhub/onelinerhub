# How do I use the scope.apply() method in AngularJS?
// plain

The `scope.apply()` method is used in AngularJS to execute an expression in the context of the current scope. This allows the model and view to be kept in sync, and it is especially useful when working with asynchronous events.

For example, if a user clicks a button, the following code can be used to update the model:

```javascript
$scope.clickButton = function() {
    $scope.value = 'clicked';
    $scope.$apply();
};
```

The `$scope.$apply()` call will cause the model to be updated, and the view will be updated accordingly.

The `scope.apply()` method is also useful for wrapping external callbacks in AngularJS context. For example, the following code will execute the `onChange` callback within the current scope:

```javascript
$scope.onChange = function(value) {
    $scope.value = value;
};

externalService.registerCallback($scope.$apply.bind($scope, $scope.onChange));
```

## Code explanation


1. `$scope.clickButton = function() { ... }` - this function is called when the user clicks a button and updates the model
2. `$scope.$apply()` - this call updates the model and causes the view to be updated
3. `$scope.onChange = function(value) { ... }` - this function is called when the external service reports a change in the value
4. `externalService.registerCallback($scope.$apply.bind($scope, $scope.onChange))` - this call wraps the `onChange` callback in the current scope

## Helpful links

- [AngularJS Documentation - Scope](https://docs.angularjs.org/api/ng/type/$rootScope.Scope)
- [AngularJS Documentation - Understanding Scopes](https://docs.angularjs.org/guide/scope)

onelinerhub: [How do I use the scope.apply() method in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-scope-apply---method-in-angularjs)