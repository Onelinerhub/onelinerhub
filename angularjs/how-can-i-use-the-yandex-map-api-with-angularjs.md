# How can I use the Yandex Map API with AngularJS?
// plain

You can use the Yandex Map API with AngularJS by using the [Yandex Maps AngularJS Wrapper Library](https://github.com/ymaps/angular-yandex-maps). This library provides an easy way to integrate the Yandex Maps API with AngularJS.

Here is an example of how to use the library to display a map:

```
<div ng-controller="MyCtrl">
  <yandex-map center="map.center" zoom="map.zoom">
  </yandex-map>
</div>

<script>
  angular.module('myapp', ['ymaps'])
    .controller('MyCtrl', function ($scope) {
      $scope.map = {
        center: [55.75, 37.57],
        zoom: 9
      };
    });
</script>
```

This code will display a map with the center coordinates of 55.75, 37.57 and a zoom level of 9.

## Code explanation


- `<div ng-controller="MyCtrl">`: This is the AngularJS controller for the map.
- `<yandex-map center="map.center" zoom="map.zoom">`: This is the directive for the map. It takes two attributes, `center` and `zoom` and sets them to the `map.center` and `map.zoom` variables.
- `angular.module('myapp', ['ymaps'])`: This is the AngularJS module for the application. It includes the `ymaps` library, which is needed to use the Yandex Maps API.
- `$scope.map = { center: [55.75, 37.57], zoom: 9 };`: This is the scope variable for the map. It sets the center coordinates and zoom level.

For more information, see the [Yandex Maps AngularJS Wrapper Library documentation](https://github.com/ymaps/angular-yandex-maps/blob/master/README.md).

onelinerhub: [How can I use the Yandex Map API with AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-the-yandex-map-api-with-angularjs)