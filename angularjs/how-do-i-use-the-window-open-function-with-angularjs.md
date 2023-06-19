# How do I use the window.open function with AngularJS?
// plain

The `window.open` function is a powerful tool that can be used to open a new browser window within an AngularJS application. To use it, you must first include the `$window` service in your controller.

```js
angular.module('myModule', [])
  .controller('myController',
    function($scope, $window) {
      $scope.openWindow = function() {
        $window.open('http://www.example.com', '_blank', 'width=400,height=400');
      };
    });
```

The `window.open` function takes three parameters: the URL to open, the window name, and a list of window features. In the example above, the URL is `http://www.example.com`, the window name is `_blank`, and the features are `width=400,height=400`.

You can also use the `window.open` function to open a new window with an AngularJS template.

```js
angular.module('myModule', [])
  .controller('myController',
    function($scope, $window) {
      $scope.openWindow = function() {
        $window.open('template.html', '_blank', 'width=400,height=400');
      };
    });
```

In this example, the URL is `template.html`, which is an AngularJS template. The window name is `_blank`, and the features are `width=400,height=400`.

For more information, see the [MDN window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) documentation.

onelinerhub: [How do I use the window.open function with AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-window-open-function-with-angularjs)