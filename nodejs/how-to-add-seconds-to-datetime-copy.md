# How to add seconds to date/time COPY

```js
let dt = new Date();
dt.setTime(dt.getTime() + 10 * 1000);

```

- `new Date` - create date/time management object
- `.setTime(` - sets unix timestamp in milliseconds
- `.getTime()` - returns unix timestamp in milliseconds
- `+ 10` - number of seconds to add to our time
- `1000` - convert second to milliseconds

group: date

## Example: 
```js
let dt = new Date();
console.log(dt)

dt.setTime(dt.getTime() + 10 * 1000);
console.log(dt)
```
```
2022-08-11T09:57:04.376Z
2022-08-11T09:57:14.376Z

```

