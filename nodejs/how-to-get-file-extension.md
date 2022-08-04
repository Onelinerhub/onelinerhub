# How to get file extension

```js
const path = require('path');
let ext = path.extname('image.png');
```

- `require('path')` - module to work with file/dir path
- `.extname(` - returns extension of a given path string
- `image.png` - sample file path to get extension from

group: path

## Example: 
```js
const path = require('path');
let ext = path.extname('image.png');
console.log(ext)
```
```
.png

```

