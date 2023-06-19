# How do I use AngularJS to create a websocket example?
// plain

Using AngularJS to create a websocket example involves the following steps:

1. Include the `AngularJS` library in your HTML page:
```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script>
```

2. Create an AngularJS `module` and inject the `$websocket` service:
```javascript
var app = angular.module('myApp', ['ngWebSocket']);
```

3. Create a `service` to establish a websocket connection with the server:
```javascript
app.service('myService', function($websocket) {
  var dataStream = $websocket('ws://localhost:8080/');

  var collection = [];

  dataStream.onMessage(function(message) {
    collection.push(JSON.parse(message.data));
  });

  var methods = {
    collection: collection,
    get: function() {
      dataStream.send(JSON.stringify({ action: 'get' }));
    }
  };

  return methods;
});
```

4. Inject the `myService` service into the controller:
```javascript
app.controller('myCtrl', function($scope, myService) {
  $scope.collection = myService.collection;
});
```

5. Use the `myService.get()` method to get data from the server:
```javascript
myService.get();
```

6. Bind the `collection` to the view to display the data:
```html
<div ng-controller="myCtrl">
  <ul>
    <li ng-repeat="item in collection">{{item}}</li>
  </ul>
</div>
```

7. Finally, open the websocket connection:
```javascript
dataStream.onOpen(function() {
  console.log('connection is opened');
});
```

**Output**: `connection is opened`

## Helpful links
- [AngularJS $websocket service](https://docs.angularjs.org/api/ng/service/$websocket)
- [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

onelinerhub: [How do I use AngularJS to create a websocket example?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-create-a-websocket-example)