# binding

How do I use AngularJS event binding?
// plain

Event binding in AngularJS allows you to bind an event to an expression. This expression will be evaluated when the event is triggered.

For example, if you want to bind a click event to a button, you can do so as follows:

```
<button ng-click="myFunction()">Click me!</button>
```

When the button is clicked, the expression `myFunction()` will be evaluated.

The syntax for event binding is `(event)="expression"`, where `event` is the name of the event to bind to (e.g. `click`), and `expression` is the expression to evaluate when the event is triggered.

You can also pass an argument to the expression, which can be useful if you need to pass data to the expression. For example:

```
<button ng-click="myFunction(data)">Click me!</button>
```

This will pass the value of `data` to the `myFunction()` expression when the button is clicked.

Here are some useful links for more information:

* [AngularJS Event Binding](https://docs.angularjs.org/guide/expression#-event-binding-)
* [AngularJS Expressions](https://docs.angularjs.org/guide/expression)

onelinerhub: [binding

How do I use AngularJS event binding?](https://onelinerhub.com/angularjs/binding--how-do-i-use-angularjs-event-binding)