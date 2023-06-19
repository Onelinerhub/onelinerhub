# How do I use the emit function in AngularJS?
// plain

The `emit` function in AngularJS is a part of the event system and is used to send data from a child scope to a parent scope. It is typically used to communicate between controllers and directives.

## Example code

```js
// in the parent controller
$scope.$on('myEvent', function(event, data) {
  console.log(data);
});

// in the child controller
$scope.$emit('myEvent', {message: 'Hello world!'});
```

## Output example

```
{message: 'Hello world!'}
```

The code above demonstrates how to use the `emit` function. The `$on` function is used to listen for the event in the parent controller, and the `$emit` function is used to send the event from the child controller. The `$emit` function takes two arguments: the name of the event and the data to be sent.

## Code explanation


- `$scope.$on('myEvent', function(event, data) {})` - this is used to listen for the event in the parent controller. The `$on` function takes two arguments: the name of the event and a callback function which is passed the event object and the data sent from the child controller.

- `$scope.$emit('myEvent', {message: 'Hello world!'})` - this is used to send the event from the child controller. The `$emit` function takes two arguments: the name of the event and the data to be sent.

## Helpful links
- [AngularJS Event System](https://docs.angularjs.org/guide/expression#-event-)
- [AngularJS $emit](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$emit)
- [AngularJS $on](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$on)

onelinerhub: [How do I use the emit function in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-emit-function-in-angularjs)