# How can I use AngularJS to implement a location search feature?
// plain

AngularJS can be used to implement a location search feature by using the HTML5 Geolocation API. The following example code will get the current user's location and display it on the page:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Location Search</title>
  </head>
  <body>
    <div ng-app="locationSearch" ng-controller="locationCtrl">
      <h1>Location Search</h1>
      <p>{{location}}</p>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script>
    <script>
      angular.module('locationSearch', [])
        .controller('locationCtrl', function($scope) {
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
              $scope.$apply(function() {
                $scope.location = "Latitude: " + position.coords.latitude +
                                  " Longitude: " + position.coords.longitude;
              });
            });
          }
        });
    </script>
  </body>
</html>
```

## Output example


Latitude: 37.78825 Longitude: -122.4324

The code consists of the following parts:

1. An HTML page with the `ng-app` directive and a `ng-controller` directive to define the AngularJS application and controller.
2. A script tag to include the AngularJS library.
3. An AngularJS application and controller to get the current user's location and display it on the page.

## Helpful links

- [HTML5 Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
- [AngularJS](https://angularjs.org/)

onelinerhub: [How can I use AngularJS to implement a location search feature?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-implement-a-location-search-feature)