# How do I use ng-click in AngularJS?
// plain

The `ng-click` directive is used to assign custom behavior to an element when it is clicked. This behavior is typically defined as a function that is declared in the scope of the controller.

For example, the following code defines a function called `sayHello` which will be called when the button is clicked:

```html
<button ng-click="sayHello()">Say Hello</button>
```

```js
$scope.sayHello = function() {
  alert('Hello!');
};
```

When the button is clicked, the `sayHello` function will be executed, and an alert will be displayed with the message `Hello!`.

The `ng-click` directive can also be used to call functions with parameters. For example, the following code will call the `showMessage` function with the parameter `'Hello world!'` when the button is clicked:

```html
<button ng-click="showMessage('Hello world!')">Show Message</button>
```

```js
$scope.showMessage = function(message) {
  alert(message);
};
```

When the button is clicked, the `showMessage` function will be called with the parameter `'Hello world!'`, and an alert will be displayed with the message `Hello world!`.

## Helpful links
- https://docs.angularjs.org/api/ng/directive/ngClick
- https://www.w3schools.com/angular/angular_events.asp

onelinerhub: [How do I use ng-click in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-ng-click-in-angularjs)