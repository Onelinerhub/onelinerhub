# How to get UTC timestamp

```js
const ts = new Date().getTime();
```

- `new Date()` - creates date/time management object based on current time
- `.getTime()` - returns UTC timestamp in milliseconds

group: timestamp

## Example: 
```js
const ts = new Date().getTime();
console.log(ts);
```
```
1660209217324

```

