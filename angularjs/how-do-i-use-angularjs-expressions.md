# How do I use AngularJS expressions?
// plain

AngularJS expressions are JavaScript-like code snippets that are used to bind application data to HTML. They are written inside double braces like `{{ expression }}`.

For example, the following expression `{{ 5 + 5 }}` will output `10` when evaluated:
```
{{ 5 + 5 }}

## Output example
 10
```

The expression can be a single variable, a property of an object, or any valid JavaScript expression such as an arithmetic expression, a logical expression, or a function call.

For example, the following expression `{{ user.name }}` will output the `name` property of the `user` object when evaluated:
```
var user = { name: 'John', age: 30 };

{{ user.name }}

## Output example
 John
```

AngularJS expressions can also contain filters that can be used to format data. For example, the following expression `{{ price | currency }}` will output the `price` variable as a currency when evaluated:

```
var price = 10;

{{ price | currency }}

## Output example
 $10.00
```

For more information on AngularJS expressions, please refer to the [AngularJS documentation](https://docs.angularjs.org/guide/expression).

onelinerhub: [How do I use AngularJS expressions?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-expressions)