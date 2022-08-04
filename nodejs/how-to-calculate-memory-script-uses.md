# How to calculate memory script uses

```js
let arr = [];
for ( let i = 0; i < 100000; i++ ) arr.push(i);
console.log(process.memoryUsage().heapUsed);
```

- `process.memoryUsage()` - returns memory usage stats
- `heapUsed` - returns amount of memory in bytes current process has used

## Example: 
```js
let arr = [];
for ( let i = 0; i < 100000; i++ ) arr.push(i)
console.log(process.memoryUsage().heapUsed);
```
```
6646080

```

