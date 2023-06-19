# How do I use the orderBy filter in AngularJS?
// plain

The `orderBy` filter in AngularJS is used to sort an array of objects by one or more of their properties. The syntax for using this filter is: `{{ orderBy_expression | orderBy : expression : reverse}}`.

The `expression` is a string that represents the property that you wish to sort by. The `reverse` is a Boolean value that determines whether the array should be sorted in ascending (`false`) or descending (`true`) order.

For example, the following code block sorts an array of objects by their `name` property in ascending order:
```
<div ng-app="myApp" ng-controller="myCtrl">
    <ul>
        <li ng-repeat="x in names | orderBy:'name':false">
            {{x.name}}
        </li>
    </ul>
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.names = [
        {name: 'John', age: 25},
        {name: 'Jane', age: 30},
        {name: 'Mary', age: 28}
    ];
});
</script>
```

The output of this code is:
```
John
Jane
Mary
```

### Explanation

1. `ng-repeat` - The `ng-repeat` directive is used to iterate over an array of objects and display its contents.
2. `orderBy` - The `orderBy` filter is used to sort an array of objects by one or more of their properties.
3. `expression` - The `expression` is a string that represents the property that you wish to sort by.
4. `reverse` - The `reverse` is a Boolean value that determines whether the array should be sorted in ascending (`false`) or descending (`true`) order.

### Relevant Links

- [AngularJS Docs - orderBy Filter](https://docs.angularjs.org/api/ng/filter/orderBy)
- [W3Schools - AngularJS orderBy Filter](https://www.w3schools.com/angular/angular_filters.asp)

onelinerhub: [How do I use the orderBy filter in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-orderby-filter-in-angularjs)