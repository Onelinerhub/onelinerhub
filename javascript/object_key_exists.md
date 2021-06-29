# check if object key exists

```javascript
 const object_key_exists = (obj, key) => {
    if(!(typeof obj === 'object' && obj !== null)) return false;
    return Object.keys(obj).includes(key);
 }
```

- object_key_exists - checks if an object contains the supplied key, returns true if the object contains that key, false otherwise.
- obj - `Object`: the object to check its keys.
- key - `String`: the key to check its existense in the object.

## examples:

```js
const obj = { a: 1, b:2};
object_key_exists(obj, 'a'); //true
object_key_exists(obj, 'c'); //false
object_key_exists([], 'a'); //false
object_key_exists([], null); //false
```
