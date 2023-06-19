# ization

How do I capitalize the first letter of a string in AngularJS?
// plain

To capitalize the first letter of a string in AngularJS, you can use the `uppercase` filter. This filter takes a string as an argument and returns the string with the first letter capitalized.

For example, the following code block:
```
<p>{{ 'hello world' | uppercase }}</p>
```

will output the following:
```
Hello world
```

## Code explanation

- `<p>`: This is an HTML tag that defines a paragraph block.
- `{{` and `}}`: These are AngularJS expressions that indicate that the content within them should be evaluated as an expression.
- `'hello world'`: This is the string that will be passed to the `uppercase` filter.
- `|`: This is the AngularJS filter operator, which indicates that the content on the left should be passed to the filter on the right.
- `uppercase`: This is the `uppercase` filter, which takes a string as an argument and returns the string with the first letter capitalized.

Here are some ## Helpful links
- [AngularJS Documentation: Filters](https://docs.angularjs.org/guide/filter)
- [AngularJS Documentation: Expressions](https://docs.angularjs.org/guide/expression)

onelinerhub: [ization

How do I capitalize the first letter of a string in AngularJS?](https://onelinerhub.com/angularjs/ization--how-do-i-capitalize-the-first-letter-of-a-string-in-angularjs)