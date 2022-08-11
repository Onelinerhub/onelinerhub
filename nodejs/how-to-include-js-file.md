# How to include js file

### We assume that `/path/to/my_lib.js` has something [exported already](/nodejs/how-to-export-class), so it can be used in main program:

```js
let my_lib = require('/path/to/my_lib.js');
```

- `/path/to/my_lib.js` - path to `JS` file to include
- `require(` - includes components from a given file
- `my_lib` - name to access included components


