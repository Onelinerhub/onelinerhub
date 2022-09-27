# How to add hours to date/time

```js
let dt = new Date();
dt.setTime(dt.getTime() + 5 * 60*60*1000);

```

- `new Date` - create date/time management object
- `.setTime(` - sets unix timestamp in milliseconds
- `.getTime()` - returns unix timestamp in milliseconds
- `5` - number of hours to add to our time
- `60*60*1000` - convert hour to milliseconds

group: date

## Example: 
```js
let dt = new Date();
console.log(dt)

dt.setTime(dt.getTime() + 5 * 60*60*1000);
console.log(dt)
```
```
2022-08-11T09:53:56.897Z
2022-08-11T14:53:56.897Z

```

link_youtube: https://youtu.be/LopOJNSkyEE
