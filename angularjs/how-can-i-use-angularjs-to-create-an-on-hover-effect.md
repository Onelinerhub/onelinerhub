# How can I use AngularJS to create an on hover effect?
// plain

An on hover effect can be created using AngularJS by using the `ng-mouseover` directive. The `ng-mouseover` directive is used to define an expression to be executed when the mouse cursor is hovered over the specified element.

For example, the following code will display an alert message when the mouse cursor is hovered over the `<div>` element:

```
<div ng-mouseover="myFunction()">Hover over me!</div>

<script>
    function myFunction() {
        alert("You hovered over me!");
    }
</script>
```

When the mouse cursor is hovered over the `<div>` element, the `myFunction()` function will be executed and an alert message will be displayed.

## Code explanation


1. `<div ng-mouseover="myFunction()">Hover over me!</div>` - This part of the code defines an element with the `ng-mouseover` directive, which specifies the expression `myFunction()` to be executed when the mouse cursor is hovered over the element.

2. `function myFunction() {` - This part of the code defines the `myFunction()` function, which will be executed when the mouse cursor is hovered over the `<div>` element.

3. `alert("You hovered over me!");` - This part of the code displays an alert message when the mouse cursor is hovered over the `<div>` element.

## Helpful links

- [AngularJS ng-mouseover Directive](https://www.w3schools.com/angular/ng_ng-mouseover.asp)

onelinerhub: [How can I use AngularJS to create an on hover effect?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-create-an-on-hover-effect)