# How do I convert JSON to an object in AngularJS?
// plain

To convert JSON to an object in AngularJS, the `angular.fromJson()` function can be used. This function will take a JSON string and parse it into an object.

## Example

```
var jsonString = '{"name": "John", "age": 30}';
var jsonObject = angular.fromJson(jsonString);
```

## Output example

```
Object {name: "John", age: 30}
```

The code above will parse the JSON string into an object. The `angular.fromJson()` function takes a JSON string as the argument and returns an object.

## Code explanation

1. `var jsonString = '{"name": "John", "age": 30}';` - this is the JSON string that will be parsed into an object.
2. `var jsonObject = angular.fromJson(jsonString);` - this is the line of code that will parse the JSON string into an object.
3. `angular.fromJson()` - this is the function that will take the JSON string and parse it into an object.

## Helpful links
- [AngularJS API Reference - angular.fromJson](https://docs.angularjs.org/api/ng/function/angular.fromJson)

onelinerhub: [How do I convert JSON to an object in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-convert-json-to-an-object-in-angularjs)