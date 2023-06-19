# How do I use an AngularJS filter?
// plain

An AngularJS filter is used to format the value of an expression for display to the user. It can be used in view templates, controllers, or services.

## Example


```
<div>{{data | currency}}</div>
```

## Output example


`$10.00`

This example uses the currency filter to format the value of the `data` expression as a currency.

The filter can also be used with arguments.

## Example


```
<div>{{data | date: 'dd/MM/yyyy'}}</div>
```

## Output example


`01/06/2020`

This example uses the date filter to format the value of the `data` expression as a date with the specified format.

## Code explanation


- `data`: The expression that will be formatted.
- `currency`: The filter used to format the expression as a currency.
- `date`: The filter used to format the expression as a date.
- `'dd/MM/yyyy'`: The format argument passed to the date filter.

## Helpful links

- [AngularJS Filters](https://docs.angularjs.org/api/ng/filter)
- [AngularJS API Reference](https://docs.angularjs.org/api)

onelinerhub: [How do I use an AngularJS filter?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-filter)