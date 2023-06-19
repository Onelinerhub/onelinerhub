# How do I bind data to an AngularJS controller?
// plain

In order to bind data to an AngularJS controller, you can use the `$scope` object. `$scope` is an object that binds the controller and the view together.

## Example

```javascript
// controller
myApp.controller('myCtrl', function($scope) {
    $scope.name = 'John Doe';
});

// view
<div ng-controller="myCtrl">
    {{ name }}
</div>
```

## Output example

John Doe

The code above binds the `name` property of the `$scope` object to the view. The view will output the value of the `name` property, which is `John Doe`.

## Code explanation

* `myApp.controller('myCtrl', function($scope) { ... }` - This is the controller, which sets up the `$scope` object.
* `$scope.name = 'John Doe';` - This is the binding of the `name` property of the `$scope` object to the value `John Doe`.
* `<div ng-controller="myCtrl"> ... </div>` - This is the view, which binds the controller to the view using the `ng-controller` directive.
* `{{ name }}` - This is the expression that will output the value of the `name` property of the `$scope` object.

## Helpful links
* [AngularJS $scope](https://docs.angularjs.org/guide/scope)
* [AngularJS ng-controller](https://docs.angularjs.org/api/ng/directive/ngController)

onelinerhub: [How do I bind data to an AngularJS controller?](https://onelinerhub.com/angularjs/how-do-i-bind-data-to-an-angularjs-controller)