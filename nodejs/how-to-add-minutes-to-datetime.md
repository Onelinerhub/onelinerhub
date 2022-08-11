# How to add minutes to date/time

```js
let dt = new Date();
dt.setTime(dt.getTime() + 10 * 60*1000);

```

- `new Date` - create date/time management object
- `.setTime(` - sets unix timestamp in milliseconds
- `.getTime()` - returns unix timestamp in milliseconds
- `10` - number of minutes to add to our time
- `60*1000` - convert minute to milliseconds

group: date

## Example: 
```js
let dt = new Date();
console.log(dt)

dt.setTime(dt.getTime() + 10 * 60*1000);
console.log(dt)
```
```
2022-08-11T09:55:46.815Z
2022-08-11T10:05:46.815Z

```

