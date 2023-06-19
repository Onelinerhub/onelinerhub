# How do I add an event listener in AngularJS?
// plain

To add an event listener in AngularJS, you can use the `$on` function. This function takes two parameters, the event name and a callback function. The callback function will be executed when the event is triggered.

```javascript
// example
$scope.$on('eventName', function(event, args) {
    // do something
});
```

The callback function will receive an event object and an argument object. The argument object contains the data associated with the event.

## Code explanation


- `$scope.$on`: This is the function used to add an event listener in AngularJS.
- `'eventName'`: This is the name of the event that will be triggered.
- `function(event, args)`: This is the callback function that will be executed when the event is triggered. It receives an event object and an argument object.
- `event`: This is the event object that is passed to the callback function.
- `args`: This is the argument object that is passed to the callback function. It contains the data associated with the event.

## Helpful links

- [AngularJS $on Documentation](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$on)

onelinerhub: [How do I add an event listener in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-add-an-event-listener-in-angularjs)