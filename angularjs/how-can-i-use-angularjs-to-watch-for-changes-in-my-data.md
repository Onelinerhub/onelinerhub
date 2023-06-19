# How can I use AngularJS to watch for changes in my data?
// plain

AngularJS provides a powerful feature called $scope.$watch to watch for changes in data. The $scope.$watch takes a function as its first argument, which is called when the value being watched changes. The second argument is the value being watched.

## Example

```
$scope.$watch(function() {
    return $scope.data;
}, function(newValue, oldValue) {
    console.log("Data changed from " + oldValue + " to " + newValue);
});
```

## Output example

```
Data changed from oldValue to newValue
```

This example code uses the $scope.$watch function to watch the value of $scope.data. When the value of $scope.data changes, the function passed as the first argument is called with the new value and the old value. In this example, the function logs a message to the console with the old and new values.

The $scope.$watch function can also take an object as the second argument, which can be used to control how the watch is triggered. The object can have the following properties:

- `deep`: (boolean) Set to `true` to watch for changes in the value's properties.
- `immediate`: (boolean) Set to `true` to trigger the watch immediately on registration.
- `listener`: (function) The function to call when the value changes.

For more information, see the [AngularJS documentation](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$watch).

onelinerhub: [How can I use AngularJS to watch for changes in my data?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-watch-for-changes-in-my-data)