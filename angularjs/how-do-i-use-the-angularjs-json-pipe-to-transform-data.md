# How do I use the AngularJS JSON pipe to transform data?
// plain

The AngularJS JSON pipe is used to transform data into JSON format. It can be used to convert a JavaScript object to a JSON string.

## Example code

```
var myObject = {
  name: 'John',
  age: 24
};

var myJSONString = JSON.stringify(myObject);

console.log(myJSONString);
```

## Output example

```
{"name":"John","age":24}
```

The code above uses the `JSON.stringify()` method to convert the JavaScript object `myObject` into a JSON string. The JSON string is then logged to the console.

The AngularJS JSON pipe can also be used to convert a JSON string back into a JavaScript object.

## Example code

```
var myJSONString = '{"name":"John","age":24}';

var myObject = JSON.parse(myJSONString);

console.log(myObject);
```

## Output example

```
{ name: 'John', age: 24 }
```

The code above uses the `JSON.parse()` method to convert the JSON string `myJSONString` into a JavaScript object. The object is then logged to the console.

## Helpful links

- [JSON.stringify() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
- [JSON.parse() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)

onelinerhub: [How do I use the AngularJS JSON pipe to transform data?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-json-pipe-to-transform-data)