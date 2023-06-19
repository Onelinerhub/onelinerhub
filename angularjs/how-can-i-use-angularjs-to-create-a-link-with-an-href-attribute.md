# How can I use AngularJS to create a link with an href attribute?
// plain

To create a link with an href attribute using AngularJS, you can use the `ng-href` directive. This directive allows you to bind the href attribute of an anchor element to an expression.

For example, if you wanted to bind the href attribute to the value of a `url` variable, you could do the following:

```html
<a ng-href="{{url}}">Link</a>
```

This will output a link with the `href` attribute set to the value of the `url` variable.

The `ng-href` directive is part of the [AngularJS core](https://docs.angularjs.org/api/ng/directive/ngHref).

## Code explanation


1. `ng-href` - Directive used to bind the href attribute of an anchor element to an expression.
2. `{{url}}` - Expression used to bind the href attribute to the value of a `url` variable.

## Helpful links

- [AngularJS Core](https://docs.angularjs.org/api/ng/directive/ngHref)

onelinerhub: [How can I use AngularJS to create a link with an href attribute?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-create-a-link-with-an-href-attribute)