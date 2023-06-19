# How can I access a parent scope variable in an AngularJS controller?
// plain

In AngularJS, a controller can access the parent scope variable by using the `$scope.$parent` property. For example, given the following controller:

```javascript
app.controller('ChildCtrl', function($scope) {
  // some code here
});
```

The parent scope variable can be accessed by using the following code snippet:

```javascript
$scope.$parent.parentVariable;
```

## Code explanation

- `$scope.$parent`: the property that allows access to the parent scope
- `parentVariable`: the parent scope variable that is being accessed

## Helpful links
- [AngularJS Documentation - Scope Inheritance](https://docs.angularjs.org/guide/scope#scope-inheritance)

onelinerhub: [How can I access a parent scope variable in an AngularJS controller?](https://onelinerhub.com/angularjs/how-can-i-access-a-parent-scope-variable-in-an-angularjs-controller)