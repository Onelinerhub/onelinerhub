# How do I use the ng-init directive in AngularJS?
// plain

The `ng-init` directive in AngularJS is used to initialize data for an application before AngularJS compiles the page. It allows you to set up variables with initial values before the page is rendered.

```
<div ng-init="name='John'">
  {{name}}
</div>
```

## Output example
 `John`

The code above uses the `ng-init` directive to set the variable `name` to the value `John`. The variable `name` is then used inside the div to display the value.

## Code explanation

1. `ng-init`: The directive used to initialize data for an application before AngularJS compiles the page.
2. `name='John'`: The variable set to the value `John`.
3. `{{name}}`: The variable used to display the value.

## Helpful links
- [AngularJS ng-init Directive](https://www.w3schools.com/angular/ng_ng-init.asp)
- [AngularJS ng-init](https://docs.angularjs.org/api/ng/directive/ngInit)

onelinerhub: [How do I use the ng-init directive in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-ng-init-directive-in-angularjs)