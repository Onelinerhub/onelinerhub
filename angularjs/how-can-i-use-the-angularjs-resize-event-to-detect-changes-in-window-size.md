# How can I use the AngularJS resize event to detect changes in window size?
// plain

The AngularJS resize event can be used to detect changes in window size. To use it, you need to inject the `$window` service into your controller and then listen for the `resize` event. Here is an example code block that shows how this is done:

```javascript
app.controller('MyCtrl', function($scope, $window) {
  $scope.windowSize = {
    width: $window.innerWidth,
    height: $window.innerHeight
  };

  angular.element($window).bind('resize', function() {
    $scope.windowSize = {
      width: $window.innerWidth,
      height: $window.innerHeight
    };
  });
});
```

The code does the following:

1. Injects the `$window` service into the controller.
2. Sets the initial window size in the `$scope.windowSize` variable.
3. Binds the `resize` event to the `$window` object and updates the `$scope.windowSize` variable with the new window size when the event is triggered.

## Helpful links

- [AngularJS Documentation - $window](https://docs.angularjs.org/api/ng/service/$window)
- [AngularJS Documentation - Events](https://docs.angularjs.org/guide/events)

onelinerhub: [How can I use the AngularJS resize event to detect changes in window size?](https://onelinerhub.com/angularjs/how-can-i-use-the-angularjs-resize-event-to-detect-changes-in-window-size)