# How can I use AngularJS and Moment.js together?
// plain

AngularJS and Moment.js can be used together to create powerful web applications. Moment.js is a JavaScript library for parsing, validating, manipulating, and formatting dates and times. AngularJS is a JavaScript framework used for creating single page applications.

The following example shows how to use AngularJS and Moment.js to format a date:

```
<div ng-app="myApp" ng-controller="myCtrl">
    <p>{{ date | date : 'MM/dd/yyyy' }}</p>
</div>

<script>
    var app = angular.module('myApp', []);
    app.controller('myCtrl', function($scope) {
        $scope.date = moment().format();
    });
</script>
```

The output of the above code would be the current date in the format MM/dd/yyyy.

## Code explanation


1. `<div ng-app="myApp" ng-controller="myCtrl">` - This defines the AngularJS application and controller.
2. `<p>{{ date | date : 'MM/dd/yyyy' }}</p>` - This uses the AngularJS date filter to format the date.
3. `var app = angular.module('myApp', []);` - This creates the AngularJS application.
4. `app.controller('myCtrl', function($scope) {` - This creates the AngularJS controller.
5. `$scope.date = moment().format();` - This uses Moment.js to get the current date and assign it to the scope.

## Helpful links

- [AngularJS](https://angularjs.org/)
- [Moment.js](https://momentjs.com/)

onelinerhub: [How can I use AngularJS and Moment.js together?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-and-moment-js-together)