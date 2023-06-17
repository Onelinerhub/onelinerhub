# How do I use jQuery to loop through each element in an array?
// plain

jQuery provides an easy way to loop through an array using the `each()` function. The following example will loop through an array and print each element in the array:
```
var arr = ["apple", "banana", "cherry"];

$(arr).each(function( index ) {
  console.log( arr[index] );
});
```
## Output example

```
apple
banana
cherry
```

The example code above uses the `each()` function to loop through the `arr` array. The `each()` function takes a callback function as an argument. The callback function takes two arguments, `index` and `value`. The `index` argument is the index of the array element being processed, and the `value` is the value of the array element being processed. The `console.log()` method is used to print the value of each element in the array.

## Code explanation

* `var arr = ["apple", "banana", "cherry"];` - declares an array `arr` with three elements
* `$(arr).each(function( index ) {` - uses the `each()` function to loop through the `arr` array
* `console.log( arr[index] );` - prints the value of each element in the array

## Helpful links
* [jQuery each()](https://api.jquery.com/each/)

onelinerhub: [How do I use jQuery to loop through each element in an array?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-loop-through-each-element-in-an-array)