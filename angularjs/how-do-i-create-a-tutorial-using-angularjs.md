# How do I create a tutorial using AngularJS?
// plain

Creating a tutorial using AngularJS is a fairly simple process.

1. Include the AngularJS script in the HTML page.
```
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
```

2. Create an AngularJS module. This module will contain the code for the tutorial.
```
var myApp = angular.module('myApp', []);
```

3. Create a controller that will contain the code for the tutorial.
```
myApp.controller('myController', function($scope) {
    // tutorial code goes here
});
```

4. Add the controller to the HTML page.
```
<div ng-app="myApp" ng-controller="myController">
    <!-- tutorial content goes here -->
</div>
```

5. Add the code for the tutorial inside the controller.
```
$scope.message = "Hello World!";
```

6. Add the code to the HTML page to display the output of the tutorial.
```
<div>{{message}}</div>
```

7. Output: `Hello World!`

## Helpful links

- [AngularJS Documentation](https://angularjs.org/docs)
- [AngularJS Tutorial](https://www.tutorialspoint.com/angularjs/index.htm)

onelinerhub: [How do I create a tutorial using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-a-tutorial-using-angularjs)