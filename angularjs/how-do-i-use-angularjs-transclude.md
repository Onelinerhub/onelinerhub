# How do I use AngularJS transclude?
// plain

AngularJS transclude is a powerful directive that allows you to insert HTML content from a parent scope into a directive's template. To use it, you need to add the `ng-transclude` attribute to the element in the directive's template that you want to insert the HTML content into.

For example, if you have a directive called `myDirective` with the following template:

```
<div>
    <h1>My Directive</h1>
    <div ng-transclude></div>
</div>
```

You can use it like this:

```
<my-directive>
    <p>This content will be inserted into the directive's template.</p>
</my-directive>
```

The result of this would be:

```
<div>
    <h1>My Directive</h1>
    <div>
        <p>This content will be inserted into the directive's template.</p>
    </div>
</div>
```

The parts of the example above are:

1. `ng-transclude` attribute: This is the attribute that tells AngularJS to insert the HTML content from the parent scope into the directive's template.
2. `myDirective` directive: This is the directive that contains the template with the `ng-transclude` attribute.
3. `<p>This content will be inserted into the directive's template.</p>`: This is the HTML content that will be inserted into the directive's template.

For more information, see the [AngularJS Documentation](https://docs.angularjs.org/api/ng/directive/ngTransclude).

onelinerhub: [How do I use AngularJS transclude?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-transclude)