# How can I create an AngularJS component?
// plain

To create an AngularJS component, you need to use the `component()` method. This method takes two parameters: the component name and an object containing the component's properties.

## Example code

```
angular.module('myApp', [])
  .component('myComponent', {
    template: '<h1>Hello world!</h1>'
  });
```

The above code will create a component called `myComponent` with the template `<h1>Hello world!</h1>`.

## Code explanation


- `angular.module('myApp', [])`: This creates an AngularJS module called `myApp`.
- `.component('myComponent', {`: This creates a component called `myComponent`.
- `template: '<h1>Hello world!</h1>'`: This sets the template for the `myComponent` component.

## Helpful links

- [AngularJS Component API Reference](https://docs.angularjs.org/api/ng/function/angular.module#component)
- [AngularJS Components Tutorial](https://www.tutorialspoint.com/angularjs/angularjs_components.htm)

onelinerhub: [How can I create an AngularJS component?](https://onelinerhub.com/angularjs/how-can-i-create-an-angularjs-component)