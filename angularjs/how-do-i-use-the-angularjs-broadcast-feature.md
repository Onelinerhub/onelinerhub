# How do I use the AngularJS broadcast feature?
// plain

The `$broadcast` feature of AngularJS allows you to emit an event from a parent scope to all of its child scopes. This is useful for passing data between scopes.

Here is an example of how to use it:

```javascript
// Parent controller
$scope.$broadcast('MyEvent', {
  someData: 'data to pass to child scope'
});

// Child controller
$scope.$on('MyEvent', function(event, args) {
  console.log(args.someData); // 'data to pass to child scope'
});
```

The first argument of the `$broadcast` function is the name of the event, and the second argument is the data to pass. This data will be passed to the `$on` function as its second argument.

In the example above, the parent scope broadcasts an event called `MyEvent` with some data. The child scope then listens for this event using the `$on` function, and logs the data to the console.

Here are some ## Helpful links

- [AngularJS Documentation - $broadcast](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$broadcast)
- [AngularJS Documentation - $on](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$on)

onelinerhub: [How do I use the AngularJS broadcast feature?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-broadcast-feature)