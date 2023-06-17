# How do I use the jQuery filter function?
// plain

The jQuery filter function is used to filter out elements from an array or object. It takes a function as an argument which is used to filter out the elements. The syntax for the filter function is:

```
var filtered = arr.filter(function(element){
    //some logic
    return boolean;
});
```

Here `arr` is the array or object to be filtered. The function passed as argument takes a single element from the array and returns a boolean value. If the boolean value is `true` then the element is included in the filtered array, otherwise it is excluded.

For example, if we have an array of numbers and we want to filter out only the even numbers then we can use the filter function as follows:

```
var numbers = [1,2,3,4,5,6];
var evens = numbers.filter(function(number){
    return number % 2 == 0;
});

console.log(evens); //output: [2,4,6]
```

The code above takes the array `numbers` and filters out only the even numbers using the filter function. The output of the code is `[2,4,6]`.

The parts of the code are:

1. `numbers`: This is the array of numbers to be filtered.
2. `evens`: This is the filtered array which contains only the even numbers.
3. `number % 2 == 0`: This is the logic used to filter out the even numbers. It checks if the number is divisible by 2 and returns `true` if it is, otherwise `false`.
4. `return boolean`: This is the return statement which returns the boolean value depending on the logic.

For more information on the jQuery filter function, refer to the following links:

1. [jQuery filter function](https://api.jquery.com/filter/)
2. [MDN filter function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

onelinerhub: [How do I use the jQuery filter function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-filter-function)