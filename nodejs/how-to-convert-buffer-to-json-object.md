# How to convert Buffer to JSON object

```js
let json = JSON.parse(buf.toString()
```

- `buf` - Buffer that [contains JSON string](https://onelinerhub.com/nodejs/how-to-convert-json-to-buffer)
- `SON.parse(` - parses given JSON and converts it into object

group: json

## Example: 
```js
const json = {name: 'Joe', age: 98};
let buf = Buffer.from(JSON.stringify(json));
console.log(JSON.parse(buf.toString()))
```
```
{ name: 'Joe', age: 98 }

```

link_youtube: https://youtu.be/TELbVEOFuX4
