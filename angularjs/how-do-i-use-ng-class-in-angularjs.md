# How do I use ng-class in AngularJS?
// plain

`ng-class` is an AngularJS directive used to dynamically set CSS classes on an HTML element. It is used to conditionally apply one or more CSS classes to an HTML element.

## Example

```
<div ng-class="{'active': isActive}">This div will be styled if isActive is true.</div>
```

The `ng-class` directive takes an object as an argument. The object keys are CSS classes and the object values are boolean expressions. If the expression evaluates to true, the corresponding CSS class is added to the element.

## Code explanation

- `<div>`: HTML element to which the `ng-class` directive is applied.
- `ng-class`: AngularJS directive.
- `{'active': isActive}`: The object argument passed to the `ng-class` directive. The key is the CSS class, and the value is a boolean expression.
- `isActive`: Boolean expression evaluated by the `ng-class` directive.

## Helpful links
- [ngClass Documentation](https://docs.angularjs.org/api/ng/directive/ngClass)
- [AngularJS Tutorial - ngClass](https://www.tutorialspoint.com/angularjs/angularjs_ng_class.htm)

onelinerhub: [How do I use ng-class in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-ng-class-in-angularjs)