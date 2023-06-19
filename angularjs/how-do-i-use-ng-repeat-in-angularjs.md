# How do I use ng-repeat in AngularJS?
// plain

Ng-Repeat is an AngularJS Directive that allows you to iterate through a collection of data and create a new HTML element for each item in the collection. It is a powerful tool to quickly generate HTML elements with data from the scope.

## Example code

```
<div ng-controller="MyCtrl">
  <ul>
    <li ng-repeat="item in items">
      {{ item }}
    </li>
  </ul>
</div>

<script>
  var app = angular.module('myApp', []);
  app.controller('MyCtrl', function($scope) {
    $scope.items = [1,2,3,4,5];
  });
</script>
```

## Output example

```
1
2
3
4
5
```

The code above will iterate through the items array in the scope and create a new `<li>` element for each item in the array. The `ng-repeat` directive will take the value of the `item` variable inside the `<li>` element and replace it with the value of each item in the array.

## Code explanation


1. `<div ng-controller="MyCtrl">` - This is the directive that tells AngularJS to use the `MyCtrl` controller.
2. `<li ng-repeat="item in items">` - This is the directive that tells AngularJS to loop through the `items` array in the scope and create a new `<li>` element for each item in the array.
3. `{{ item }}` - This is the expression that tells AngularJS to take the value of the `item` variable and replace it with the value of each item in the array.
4. `var app = angular.module('myApp', []);` - This is the code that creates an AngularJS module with the name `myApp`.
5. `app.controller('MyCtrl', function($scope) {` - This is the code that creates the `MyCtrl` controller.
6. `$scope.items = [1,2,3,4,5];` - This is the code that creates an array of items in the scope.

## Helpful links

- [Official AngularJS ng-repeat Documentation](https://docs.angularjs.org/api/ng/directive/ngRepeat)
- [AngularJS ng-repeat Tutorial](https://www.tutorialspoint.com/angularjs/angularjs_ng_repeat_directive.htm)

onelinerhub: [How do I use ng-repeat in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-ng-repeat-in-angularjs)