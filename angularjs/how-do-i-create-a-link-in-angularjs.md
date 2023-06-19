# How do I create a link in AngularJS?
// plain

Creating a link in AngularJS is done with the `<a>` element and the `ng-href` directive. The `ng-href` directive allows you to set the `href` attribute of an `<a>` element dynamically.

For example, the following code creates a link to `https://www.example.com`:

```
<a ng-href="https://www.example.com">Example</a>
```

This code will output the following HTML:

```
<a href="https://www.example.com">Example</a>
```

The `ng-href` directive is useful for creating dynamic links. For example, the following code creates a link based on a variable:

```
<a ng-href="{{url}}">Example</a>
```

If the `url` variable is set to `https://www.example.com`, the output HTML will be:

```
<a href="https://www.example.com">Example</a>
```

The `ng-href` directive is useful for creating dynamic links in AngularJS applications.

## Helpful links

- [AngularJS ng-href Directive Documentation](https://docs.angularjs.org/api/ng/directive/ngHref)

onelinerhub: [How do I create a link in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-a-link-in-angularjs)