# How to pretty print JSON stringify

```js
const json = {name: 'Joe', age: 98};
const pretty = JSON.stringify(json, null, 2)
```

- `{name: 'Joe', age: 98}` - sample JSON to encode and pretty print
- `JSON.stringify(` - convert given object to JSON string
- `2` - indent size to use for JSON formatting (`2` spaces in our case)

group: json

## Example: 
```js
const json = {
  name: 'Joe', age: 98,
  location: {name: 'USA'}
};
const pretty = JSON.stringify(json, null, 2)
console.log(pretty)
```
```
{
  "name": "Joe",
  "age": 98,
  "location": {
    "name": "USA"
  }
}

```

