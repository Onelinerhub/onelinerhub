# How do I use an AngularJS datepicker?
// plain

To use an AngularJS datepicker, you first need to include the necessary AngularJS and datepicker library files. Then, you need to create an HTML element to contain the datepicker, such as a `<div>` or `<input>` element.

Next, you need to create an AngularJS app and controller, which will contain the logic to initialize and use the datepicker. In the controller, you need to define an object to store the selected date, and then use the `datepicker-options` attribute to configure the datepicker.

Here is an example of how to use an AngularJS datepicker:

```
<div ng-app="myApp" ng-controller="myCtrl">
  <input type="text" ng-model="date" datepicker-options="dateOptions" />
</div>

<script>
  angular.module("myApp", [])
    .controller("myCtrl", function($scope) {
      $scope.date = new Date();
      $scope.dateOptions = {
        formatYear: 'yy',
        startingDay: 1
      };
    });
</script>
```

This will create an input element with a datepicker, initialized with the current date.

The `datepicker-options` attribute is used to configure the datepicker. The available options are:
- `formatYear`: The format of the year in the datepicker header.
- `startingDay`: The day of the week to start the datepicker on.
- `minDate`: The minimum selectable date.
- `maxDate`: The maximum selectable date.
- `initDate`: The initial date to display in the datepicker.

For more information, see the [AngularJS datepicker documentation](https://angular-ui.github.io/bootstrap/#/datepicker).

onelinerhub: [How do I use an AngularJS datepicker?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-datepicker)