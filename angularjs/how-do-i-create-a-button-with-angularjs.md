# How do I create a button with AngularJS?
// plain

To create a button with AngularJS, you can use `ng-click` directive. This directive will assign a function to the button, which will be triggered when the button is clicked.

For example:
```
<button ng-click="myFunction()">Click Me!</button>
```
In the controller, you will need to define the function that will be triggered when the button is clicked.

For example:
```
$scope.myFunction = function(){
  console.log("Button clicked!");
}
```
## Output example

```
Button clicked!
```

The `ng-click` directive consists of the following parts:
1. `ng-click` - This is the directive which assigns a function to the button.
2. `myFunction()` - This is the function that will be triggered when the button is clicked.
3. `$scope` - This is the scope of the controller where the function is defined.

## Helpful links
- [ng-click Directive](https://docs.angularjs.org/api/ng/directive/ngClick)
- [AngularJS Tutorial](https://www.tutorialspoint.com/angularjs/angularjs_overview.htm)

onelinerhub: [How do I create a button with AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-a-button-with-angularjs)