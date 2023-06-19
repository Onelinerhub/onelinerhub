# How do I use AngularJS component bindings?
// plain

Using component bindings in AngularJS allows you to create components that are self-contained and reusable. To use component bindings, you will need to define a component in the module's `.component()` method.

## Example

```javascript
angular.module('myApp', [])
    .component('myComponent', {
        bindings: {
            data: '<'
        },
        template: '<div>{{$ctrl.data}}</div>',
        controller: function() {
            var ctrl = this;
        }
    });
```

The `bindings` property of the component is used to define the data that will be passed to the component. In this example, `data` is passed as an input binding, indicated by the `<` symbol. The component can then access the data using the `$ctrl` controller variable.

The template property is used to define the HTML template for the component. In this example, the value of the `data` binding is displayed inside a `<div>` element.

The controller property is used to define the controller for the component. In this example, the controller is assigned to the `ctrl` variable.

## Helpful links

- [AngularJS Component](https://docs.angularjs.org/guide/component)
- [AngularJS Components](https://www.w3schools.com/angular/angular_components.asp)

onelinerhub: [How do I use AngularJS component bindings?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-component-bindings)