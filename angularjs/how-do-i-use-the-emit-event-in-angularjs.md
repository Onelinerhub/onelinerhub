# How do I use the emit event in AngularJS?
// plain

The `$emit` event is an important part of AngularJS which allows you to send messages up the scope hierarchy. It is used to notify the parent controllers of events that have occurred in the child controllers.

Below is an example of how to use the `$emit` event in AngularJS.

```
// Child Controller
app.controller('ChildController', function($scope) {
  $scope.sendMessage = function() {
    $scope.$emit('myEvent', 'Hello World!');
  };
});

// Parent Controller
app.controller('ParentController', function($scope) {
  $scope.$on('myEvent', function(event, data) {
    console.log(data); // Output: 'Hello World!'
  });
});
```

The code above shows how to use the `$emit` event in AngularJS. The `ChildController` emits a message which is then caught by the `ParentController`. The `$on` method is used to listen for the `$emit` event.

The list below explains the parts of the code above:

- `$scope.$emit('myEvent', 'Hello World!')`: This is used to emit a message from the `ChildController` to the `ParentController`.
- `$scope.$on('myEvent', function(event, data)`: This is used to listen for the `$emit` event from the `ChildController` in the `ParentController`.
- `console.log(data)`: This logs the data that is sent from the `ChildController` to the `ParentController`.

## Helpful links

- [AngularJS $emit](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$emit)
- [AngularJS $on](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$on)

onelinerhub: [How do I use the emit event in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-emit-event-in-angularjs)