# How do I implement drag and drop functionality using AngularJS?
// plain

To implement drag and drop functionality using AngularJS, you can use the HTML5 Drag and Drop API. The following code example demonstrates how to use the API for drag and drop functionality in AngularJS:

```
<div ng-app="myApp" ng-controller="myCtrl">
  <div ng-drag="true" ng-drag-data="myData">Drag Me</div>
  <div ng-drop="true" ng-drop-success="onDropComplete($data,$event)">Drop Here</div>
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
  $scope.myData = {data: 'myData'};
  $scope.onDropComplete = function (data,evt) {
    console.log("drop success, data:", data);
  }
});
</script>
```

This code example will create two div elements, one with the `ng-drag` directive and one with the `ng-drop` directive. When the `ng-drag` element is dragged and dropped onto the `ng-drop` element, the `onDropComplete` function will be called with the data from the `ng-drag` element and the event object as parameters.

## Code explanation


1. `ng-app="myApp"`: This directive defines the AngularJS application.
2. `ng-controller="myCtrl"`: This directive defines the controller for the application.
3. `ng-drag="true"` and `ng-drop="true"`: These directives enable the drag and drop functionality.
4. `ng-drag-data="myData"`: This directive sets the data to be transferred when the element is dragged.
5. `ng-drop-success="onDropComplete($data,$event)"`: This directive sets the function to be called when the element is dropped.

For more information on implementing drag and drop functionality using AngularJS, see the [AngularJS Drag and Drop](https://www.w3schools.com/angular/angular_dnd.asp) tutorial.

onelinerhub: [How do I implement drag and drop functionality using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-implement-drag-and-drop-functionality-using-angularjs)