# How can I implement XSS protection in an AngularJS application?
// plain

XSS protection in an AngularJS application can be implemented in the following ways:

1. Using the `$sce` service to sanitize HTML:
```javascript
// Inject the $sce service
var app = angular.module('myApp', ['ngSanitize']);

// Use the $sce service to sanitize HTML
app.controller('myCtrl', function($scope, $sce) {
   $scope.safeHTML = $sce.trustAsHtml("<h1>Hello World!</h1>");
});
```

2. Using the `ngSanitize` module to sanitize HTML:
```javascript
// Inject the ngSanitize module
var app = angular.module('myApp', ['ngSanitize']);

// Use the ngSanitize module to sanitize HTML
app.controller('myCtrl', function($scope, $sanitize) {
   $scope.safeHTML = $sanitize("<h1>Hello World!</h1>");
});
```

3. Using the `ng-bind-html` directive to sanitize HTML:
```html
<!-- Use the ng-bind-html directive to sanitize HTML -->
<div ng-controller="myCtrl">
  <div ng-bind-html="safeHTML"></div>
</div>
```

These are the three main approaches to implementing XSS protection in an AngularJS application. For more information, please refer to the following links:

* [$sce - AngularJS](https://docs.angularjs.org/api/ng/service/$sce)
* [ngSanitize - AngularJS](https://docs.angularjs.org/api/ngSanitize)
* [ngBindHtml - AngularJS](https://docs.angularjs.org/api/ng/directive/ngBindHtml)

onelinerhub: [How can I implement XSS protection in an AngularJS application?](https://onelinerhub.com/angularjs/how-can-i-implement-xss-protection-in-an-angularjs-application)