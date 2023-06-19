# How do I use the AngularJS filter pipe?
// plain

The AngularJS filter pipe is used to filter an array of data to return a subset of the data that meets certain criteria.

## Example


```
<div ng-app="myApp" ng-controller="MyController">
  <ul>
    <li ng-repeat="person in people | filter:myFilter">
      {{ person.name }}
    </li>
  </ul>
</div>

<script>
  var app = angular.module('myApp', []);

  app.controller('MyController', function($scope) {
    $scope.people = [
      {name: 'John', age: 25},
      {name: 'Jane', age: 30},
      {name: 'Jim', age: 27}
    ];
    $scope.myFilter = function(person) {
      return person.age > 25;
    };
  });
</script>
```

## Output example

* Jane
* Jim

The code above uses the AngularJS filter pipe to filter the array of people and return only the people with an age greater than 25.

The code consists of the following parts:

1. A `<div>` element with an `ng-app` and `ng-controller` attribute to define the application and controller.
2. An `<ul>` element with an `ng-repeat` attribute to loop through each item in the `people` array.
3. A `filter:myFilter` expression in the `ng-repeat` attribute to use the `myFilter` function to filter the `people` array.
4. A `$scope.people` array of objects with each object containing a `name` and `age` property.
5. A `$scope.myFilter` function to filter the `people` array and return only the people with an age greater than 25.

For more information on the AngularJS filter pipe, see the [AngularJS documentation](https://docs.angularjs.org/api/ng/filter/filter).

onelinerhub: [How do I use the AngularJS filter pipe?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-filter-pipe)