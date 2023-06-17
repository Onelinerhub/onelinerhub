# How do I encode JSON using jQuery?
// plain

jQuery provides a built-in function for encoding JSON strings. The `JSON.stringify()` method takes a JavaScript object and converts it into a JSON string.

```
var myObj = { name: 'John', age: 30 };
var myJson = JSON.stringify(myObj);
console.log(myJson);
```

## Output example

```
{"name":"John","age":30}
```

The `JSON.stringify()` method has two optional parameters:

1. `replacer` - A function that alters the behavior of the stringification process, or an array of String and Number objects that serve as a whitelist for selecting/filtering the properties of the value object to be included in the JSON string.
2. `space` - A String or Number object that's used to insert white space into the output JSON string for readability purposes.

For more information, see the [jQuery documentation](https://api.jquery.com/jQuery.parseJSON/) and [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

onelinerhub: [How do I encode JSON using jQuery?](https://onelinerhub.com/jquery/how-do-i-encode-json-using-jquery)