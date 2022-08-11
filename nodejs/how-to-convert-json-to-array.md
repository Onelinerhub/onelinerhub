# How to convert JSON to array

```js
const json = {name: 'Joe', age: 98};
const array = Object.values(json);
```

- `{name: 'Joe', age: 98}` - sample JSON object to convert to array
- `Object.values(` - return all values as array from given object
- `array` - will contain `json` values list as array

group: json

## Example: 
```js
const json = {name: 'Joe', age: 98};
const array = Object.values(json);
console.log(array);
```
```
[ 'Joe', 98 ]

```

