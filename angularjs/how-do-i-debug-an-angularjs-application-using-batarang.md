# How do I debug an AngularJS application using Batarang?
// plain

Debugging an AngularJS application using Batarang is a straightforward process. Batarang is a Chrome extension that allows you to debug and profile AngularJS applications. Here are the steps to debug an AngularJS application using Batarang:

1. Install the Batarang Chrome extension.
2. Open the application you want to debug in Chrome.
3. Open the Batarang panel by clicking on the Batarang icon in the Chrome DevTools.
4. Select the AngularJS tab.
5. Select the application you want to debug.
6. Start debugging by selecting the elements you want to inspect.
7. Use the Batarang console to view errors and debug your application.

## Example code


```
// AngularJS code
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.name = "John";
});
```

## Output example


No output.

The code above is a basic AngularJS application. The app variable is used to create an AngularJS module. The controller is then used to create a controller for the application. The name variable is then set to a value of "John".

onelinerhub: [How do I debug an AngularJS application using Batarang?](https://onelinerhub.com/angularjs/how-do-i-debug-an-angularjs-application-using-batarang)