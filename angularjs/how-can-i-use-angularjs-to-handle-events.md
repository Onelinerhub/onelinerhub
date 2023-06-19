# How can I use AngularJS to handle events?
// plain

AngularJS provides the ng-click directive which allows you to handle events in your application. This directive can be added to any HTML element and will call a function in your controller when the element is clicked.

For example:

```html
<button ng-click="myFunction()">Click me</button>
```

The above code will call the `myFunction()` in your controller when the button is clicked.

In your controller you can define the `myFunction()` like this:

```javascript
$scope.myFunction = function() {
    alert('You clicked the button!');
};
```

When the button is clicked, the alert will be displayed:

```
You clicked the button!
```

The ng-click directive is just one of the many ways to handle events with AngularJS. You can also use `ng-change`, `ng-blur`, `ng-focus`, `ng-dblclick`, `ng-mousedown`, `ng-mouseup`, `ng-mouseenter`, `ng-mouseleave`, `ng-keydown`, `ng-keyup`, `ng-keypress` and more.

For more information, see the [AngularJS documentation](https://docs.angularjs.org/api/ng/directive/ngClick).

onelinerhub: [How can I use AngularJS to handle events?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-handle-events)