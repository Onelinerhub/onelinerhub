# How do I use the ng-if directive in AngularJS?
// plain

The ng-if directive in AngularJS is used to conditionally render an element based on a boolean expression. It is a better alternative to using the `ng-show` and `ng-hide` directives as it completely removes the element from the DOM instead of just hiding it.

Here is an example of how to use the ng-if directive:

```html
<div ng-if="user.isAdmin">
  <h2>Welcome Admin!</h2>
</div>
```

In the example above, the `<div>` element will only be rendered if the `user.isAdmin` expression is `true`.

## Code explanation


* `ng-if` - This is the directive that is used to conditionally render an element.
* `user.isAdmin` - This is the boolean expression that is evaluated to determine if the element should be rendered.

## Helpful links

* [ng-if Directive](https://docs.angularjs.org/api/ng/directive/ngIf)

onelinerhub: [How do I use the ng-if directive in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-ng-if-directive-in-angularjs)