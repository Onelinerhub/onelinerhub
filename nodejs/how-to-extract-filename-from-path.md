# How to extract filename from path

```js
const path = require('path');
let file = path.basename('/home/joe/image.png');
```

- `require('path')` - module to work with file/dir path
- `.basename(` - return filename part of a given path
- `/home/joe/image.png` - sample path to extract filename from

group: path

## Example: 
```js
const path = require('path');
let file = path.basename('/home/joe/image.png');
console.log(file)
```
```
image.png

```

