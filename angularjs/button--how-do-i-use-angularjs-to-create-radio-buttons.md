# button

How do I use AngularJS to create radio buttons?
// plain

AngularJS can be used to create radio buttons. Here is an example of how to do so:

```
<div ng-app="myApp" ng-controller="myCtrl">

  <input type="radio" ng-model="gender" value="male">Male<br>
  <input type="radio" ng-model="gender" value="female">Female

  <h1>You selected: {{gender}}</h1>

</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.gender = 'male';
});
</script>
```

This example will create two radio buttons, one for male and one for female. The ng-model directive is used to bind the value of the radio buttons to the gender variable. The value of the gender variable is then displayed in the h1 tag.

## Code explanation

- `<div ng-app="myApp" ng-controller="myCtrl">`: This line declares an AngularJS application with the name myApp and the controller myCtrl.
- `<input type="radio" ng-model="gender" value="male">Male<br>`: This line creates a radio button with the value male and binds it to the gender variable using the ng-model directive.
- `<h1>You selected: {{gender}}</h1>`: This line displays the value of the gender variable.
- `var app = angular.module('myApp', []);`: This line creates an AngularJS module named myApp.
- `app.controller('myCtrl', function($scope) {`: This line creates a controller named myCtrl.
- `$scope.gender = 'male';`: This line sets the initial value of the gender variable to male.

## Helpful links
- [AngularJS tutorial](https://www.w3schools.com/angular/)
- [AngularJS documentation](https://angularjs.org/)

onelinerhub: [button

How do I use AngularJS to create radio buttons?](https://onelinerhub.com/angularjs/button--how-do-i-use-angularjs-to-create-radio-buttons)