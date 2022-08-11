# How to convert JSON to Buffer

```js
const json = {name: 'Joe', age: 98};
let buf = Buffer.from(JSON.stringify(json));
```

- `{name: 'Joe', age: 98}` - sample JSON
- `Buffer.from` - create Buffer from given object (string in our case)
- `JSON.stringify` - convert given object to JSON string

group: json

## Example: 
```js
const json = {name: 'Joe', age: 98};
let buf = Buffer.from(JSON.stringify(json));

console.log(buf)
```
```
<Buffer 7b 22 6e 61 6d 65 22 3a 22 4a 6f 65 22 2c 22 61 67 65 22 3a 39 38 7d>

```

