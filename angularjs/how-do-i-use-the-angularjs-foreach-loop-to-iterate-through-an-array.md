# How do I use the AngularJS foreach loop to iterate through an array?
// plain

The AngularJS `foreach` loop can be used to iterate through an array. The syntax for this loop is `angular.forEach(array, iterator[, context])`.

The `array` parameter is the array to be looped through, the `iterator` parameter is a function that is called for each item in the array, and the `context` parameter is an optional object to use as the context for the iterator function.

## Example code

```
var myArray = [1,2,3,4,5];

angular.forEach(myArray, function(value, key) {
    console.log(key + ': ' + value);
});
```

## Output example

```
0: 1
1: 2
2: 3
3: 4
4: 5
```

The `value` parameter is the value of the item in the array, and the `key` parameter is the index of the item in the array.

## Helpful links

- [AngularJS foreach Loop](https://www.tutorialsteacher.com/angularjs/angularjs-foreach)
- [AngularJS API Reference - forEach](https://docs.angularjs.org/api/ng/function/angular.forEach)

onelinerhub: [How do I use the AngularJS foreach loop to iterate through an array?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-foreach-loop-to-iterate-through-an-array)