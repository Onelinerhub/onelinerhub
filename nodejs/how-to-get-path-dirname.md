# How to get path dirname

```js
const path = require('path');
let dir = path.dirname('/home/joe/image.png');
```

- `require('path')` - module to work with file/dir path
- `.dirname(` - return dir part of a given path
- `/home/joe/image.png` - sample path to return dir for

group: path

## Example: 
```js
const path = require('path');
let dir = path.dirname('/home/joe/image.png');
console.log(dir)
```
```
/home/joe

```

link_youtube: https://youtu.be/sJfNQwkG8i8
