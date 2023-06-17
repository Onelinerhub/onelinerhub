# How can I convert a jQuery JSON object to an array?
// plain

To convert a jQuery JSON object to an array, you can use the `$.map()` function. This function takes a JSON object as an argument and returns an array. The following example code will convert a JSON object to an array:

```
var myObject = {
    "name": "John",
    "age": 30,
    "city": "New York"
};

var myArray = $.map(myObject, function(value, index) {
    return [value];
});

console.log(myArray);
```

## Output example

```
["John", 30, "New York"]
```

The code above consists of three parts:

1. The `var myObject` line defines a JSON object.
2. The `var myArray` line uses the `$.map()` function to convert the JSON object to an array. The function takes two arguments, the JSON object and a callback function. The callback function takes two arguments, the value and the index of the object. In this case, we are simply returning the value.
3. The `console.log(myArray)` line logs the result of the conversion to the console.

## Helpful links

- [jQuery API Documentation - $.map()](https://api.jquery.com/jquery.map/)

onelinerhub: [How can I convert a jQuery JSON object to an array?](https://onelinerhub.com/jquery/how-can-i-convert-a-jquery-json-object-to-an-array)