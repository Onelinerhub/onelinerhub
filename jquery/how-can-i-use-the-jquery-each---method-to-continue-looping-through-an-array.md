# How can I use the jQuery each() method to continue looping through an array?
// plain

The jQuery `each()` method can be used to loop through an array. It takes a function as an argument, which is executed for each element in the array. The function has two parameters: the index of the array element and the element's value.

```
var arr = ["Apple", "Banana", "Cherry"];

$.each(arr, function(index, value) {
  console.log(index + ": " + value);
});
```

## Output example

```
0: Apple
1: Banana
2: Cherry
```

The code above will loop through the array `arr` and print out each element's index and value.

The `each()` method can be used to loop through an array until a certain condition is met. This is done by using the `return` statement inside the function. If `return` is called with the value `false`, the loop will be stopped.

```
var arr = ["Apple", "Banana", "Cherry"];

$.each(arr, function(index, value) {
  console.log(index + ": " + value);

  if (value === "Banana") {
    return false;
  }
});
```

## Output example

```
0: Apple
1: Banana
```

In the code above, the loop is stopped after the element with the value `Banana` is printed out.

The `each()` method is a useful tool for looping through an array and performing operations on each element.

## Helpful links
- [jQuery each() Method](https://www.w3schools.com/jquery/jquery_ref_traversing.asp)
- [JavaScript forEach() Method](https://www.w3schools.com/jsref/jsref_forEach.asp)

onelinerhub: [How can I use the jQuery each() method to continue looping through an array?](https://onelinerhub.com/jquery/how-can-i-use-the-jquery-each---method-to-continue-looping-through-an-array)