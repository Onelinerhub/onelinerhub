# How do I use AngularJS ng-if and else together in a single statement?
// plain

The `ng-if` and `ng-else` directives in AngularJS allow you to conditionally render a portion of the HTML based on a given expression. To use `ng-if` and `ng-else` together in a single statement, you can use the following syntax:

```
<div ng-if="expression">
    // HTML to be rendered if expression is true
</div>
<div ng-else>
    // HTML to be rendered if expression is false
</div>
```

For example, if you want to display a message if the value of a variable `name` is equal to `John`, you can use the following code:

```
<div ng-if="name == 'John'">
    Hello, John!
</div>
<div ng-else>
    Hello, stranger!
</div>
```

If the value of `name` is `John`, the output of the above code will be:

```
Hello, John!
```

If the value of `name` is something other than `John`, the output of the above code will be:

```
Hello, stranger!
```

The parts of the code are:

- `<div ng-if="expression">`: This is the opening tag of the HTML element which will be conditionally rendered. The expression inside the `ng-if` directive will be evaluated and if it evaluates to `true`, the HTML element and its content will be rendered.
- `// HTML to be rendered if expression is true`: This is the HTML content which will be rendered if the expression inside the `ng-if` directive evaluates to `true`.
- `<div ng-else>`: This is the opening tag of the HTML element which will be conditionally rendered. This HTML element and its content will be rendered if the expression inside the `ng-if` directive evaluates to `false`.
- `// HTML to be rendered if expression is false`: This is the HTML content which will be rendered if the expression inside the `ng-if` directive evaluates to `false`.

For more information about `ng-if` and `ng-else`, see [the official AngularJS documentation](https://docs.angularjs.org/api/ng/directive/ngIf).

onelinerhub: [How do I use AngularJS ng-if and else together in a single statement?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-ng-if-and-else-together-in-a-single-statement)