# How do I use different binding types in AngularJS?
// plain

In AngularJS, there are different types of bindings that can be used to bind data to HTML elements. The most commonly used bindings are the `{{ expression }}` interpolation binding and the `[property]="expression"` property binding.

#### Interpolation Binding

Interpolation binding is used to display a value from a component class. It is denoted by double curly braces `{{ }}` and is used to display a component property value.

```
<h2>Welcome {{name}}!</h2>
```

## Output example


```
Welcome John!
```

#### Property Binding

Property binding is used to set a property or an attribute of a DOM element. It is denoted by square brackets `[]` and is used to bind a component property value to a DOM property.

```
<button [disabled]="isDisabled">Submit</button>
```

In the above example, the `disabled` property of the button will be set to `true` or `false` depending on the value of the `isDisabled` property of the component class.

#### Event Binding

Event binding is used to bind an event to an event handler. It is denoted by parentheses `()` and is used to bind a component event handler to a DOM event.

```
<button (click)="onClick()">Submit</button>
```

In the above example, the `onClick()` event handler of the component class will be called when the `click` event is triggered on the button.

#### Two-Way Binding

Two-way binding is used to bind a component property value to a DOM element. It is denoted by square brackets `[]` and parentheses `()` and is used to bind a component property value to a DOM property and update the component property value when the DOM property value changes.

```
<input [(ngModel)]="name" />
```

In the above example, the value of the `name` property of the component class will be set to the value of the `input` element and the `input` element will be updated when the `name` property value changes.

## Helpful links
- [Angular Documentation - Interpolation](https://angular.io/guide/template-syntax#interpolation)
- [Angular Documentation - Property Binding](https://angular.io/guide/template-syntax#property-binding)
- [Angular Documentation - Event Binding](https://angular.io/guide/template-syntax#event-binding)
- [Angular Documentation - Two-Way Binding](https://angular.io/guide/template-syntax#two-way-binding)

onelinerhub: [How do I use different binding types in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-different-binding-types-in-angularjs)