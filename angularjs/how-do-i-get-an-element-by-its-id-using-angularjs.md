# How do I get an element by its id using AngularJS?
// plain

Getting an element by its id using AngularJS is a simple process. To do this, you must first inject the `$document` service into your controller. You can then use the `getElementById()` method of the `$document` service to get the element. Here is an example:

```javascript
angular.module('myApp', [])
  .controller('myCtrl', function($scope, $document) {
    var element = $document.getElementById('myElement');
    // Do something with the element
  });
```

The `getElementById()` method takes one parameter, which is the id of the element you want to get. In this case, it is `myElement`. The method will return the element with the corresponding id, or `null` if no element with that id exists.

The following list explains each code part in the example above:
- `angular.module('myApp', [])`: This creates an AngularJS module named `myApp`.
- `.controller('myCtrl', function($scope, $document)`: This creates a controller named `myCtrl` and injects the `$scope` and `$document` services into it.
- `var element = $document.getElementById('myElement')`: This uses the `getElementById()` method of the `$document` service to get the element with the id `myElement`.
- `// Do something with the element`: This is a comment to remind us to do something with the element.

Here are some relevant links for further reading:
- [AngularJS Documentation - $document](https://docs.angularjs.org/api/ng/service/$document)
- [MDN - Document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)

onelinerhub: [How do I get an element by its id using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-get-an-element-by-its-id-using-angularjs)