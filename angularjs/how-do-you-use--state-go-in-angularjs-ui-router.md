# How do you use $state.go in AngularJS UI-Router?
// plain

`$state.go` is a method used in AngularJS UI-Router to transition to a new state. It can be used to redirect a user from one view to another. It takes two parameters:

1. **state**: This is the name of the state that you want to transition to.
2. **params**: This is an optional parameter that can be used to pass parameters to the new state.

## Example

```javascript
$state.go('home', {
  id: 123
});
```
This code would transition the user to the `home` state, and pass the parameter `id` with the value of `123`.

## Helpful links
- [AngularJS UI-Router Documentation](https://ui-router.github.io/ng1/)
- [$state.go API Reference](https://ui-router.github.io/ng1/docs/latest/classes/transition.transition-1.html#go)

onelinerhub: [How do you use $state.go in AngularJS UI-Router?](https://onelinerhub.com/angularjs/how-do-you-use--state-go-in-angularjs-ui-router)