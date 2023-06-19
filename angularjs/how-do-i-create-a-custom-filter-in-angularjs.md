# How do I create a custom filter in AngularJS?
// plain

Creating a custom filter in AngularJS requires the use of the `filter` function. This function takes two parameters, the name of the filter, and a function that will be used to filter the data.

## Example

```
app.filter('reverse', function() {
  return function(text) {
    return text.split("").reverse().join("");
  }
});
```

## Output example

```
No output
```

The code above creates a filter called `reverse` that takes a string as an argument and returns the string in reverse order.

The filter function takes two parameters:

1. The name of the filter - `reverse`
2. The filter function - `function(text) { return text.split("").reverse().join(""); }`

The filter function takes a string as an argument and returns the string in reverse order using the split, reverse, and join functions.

Once the filter is created, it can be used in an Angular template as follows:

`{{ 'Hello World' | reverse }}`

## Output example

```
dlroW olleH
```

## Helpful links
- [AngularJS Filters](https://docs.angularjs.org/api/ng/filter)
- [AngularJS Filter Function](https://docs.angularjs.org/api/ng/filter/filter)

onelinerhub: [How do I create a custom filter in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-a-custom-filter-in-angularjs)