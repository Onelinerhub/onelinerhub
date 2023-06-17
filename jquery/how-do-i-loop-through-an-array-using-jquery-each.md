# How do I loop through an array using jQuery each?
// plain

To loop through an array using jQuery each, you can use the jQuery.each() function. This function takes two parameters, the array to loop through and a function to execute for each item in the array. The function takes two parameters, the index of the item in the array and the value of the item.

## Example code

```
var array = [1,2,3];

jQuery.each(array, function(index, value) {
  console.log(index + ': ' + value);
});
```

## Output example

```
0: 1
1: 2
2: 3
```

The above code will loop through the array and output the index of the item and its value.

Parts of the code:
- `var array = [1,2,3];` - This is the array to loop through.
- `jQuery.each(array, function(index, value) {` - This is the jQuery.each() function which takes two parameters, the array to loop through and a function to execute for each item in the array.
- `console.log(index + ': ' + value);` - This is the function to execute for each item in the array. It takes two parameters, the index of the item in the array and the value of the item.

## Helpful links
- [jQuery.each() Documentation](https://api.jquery.com/jquery.each/)

onelinerhub: [How do I loop through an array using jQuery each?](https://onelinerhub.com/jquery/how-do-i-loop-through-an-array-using-jquery-each)