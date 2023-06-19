# filter

How can I apply a filter in AngularJS?
// plain

Filtering in AngularJS can be done using the `filter` filter. This filter takes an array as input and returns a subset of that array based on the criteria specified.

## Example code

```
var fruits = [
  {name: 'apple', color: 'red'},
  {name: 'banana', color: 'yellow'},
  {name: 'grape', color: 'green'}
];

var filteredFruits = $filter('filter')(fruits, {color: 'red'});

console.log(filteredFruits);
```

## Output example

```
[{name: 'apple', color: 'red'}]
```

The code above uses the `filter` filter to filter the `fruits` array based on the criteria of `color: 'red'`. The output is an array containing only the element that matched the criteria.

## Code explanation


- `var fruits = [...]`: an array of objects containing fruit names and colors.
- `$filter('filter')(fruits, {color: 'red'})`: the `filter` filter is used to filter the `fruits` array. The criteria is specified as `{color: 'red'}`.
- `console.log(filteredFruits)`: this logs the output of the `filter` filter to the console.

## Helpful links
- [AngularJS Filter API](https://docs.angularjs.org/api/ng/filter/filter)
- [AngularJS Filter Example](https://codepen.io/anon/pen/JmGqMv)

onelinerhub: [filter

How can I apply a filter in AngularJS?](https://onelinerhub.com/angularjs/filter--how-can-i-apply-a-filter-in-angularjs)