# How to convert unix timestamp to date and time

```js
const date = new Date( 1660209124 * 1000 );
const dt = date.getFullYear() + '-' + (date.getMonth()+1) + '-' +
           date.getDate() + ' ' +
           date.getHours() + ':' + date.getMinutes() + ':' +
           date.getSeconds();
```

- `new Date` - create date/time management object
- `1660209124` - sample timestamp to convert to date
- `* 1000` - convert given timestamp from seconds to milliseconds
- `getFullYear()` - returns year from given date
- `getMonth()` - returns month
- `getDate()` - returns date
- `getHours()` - returns hours
- `getMinutes()` - returns minutes
- `getSeconds()` - returns seconds

group: timestamp

## Example: 
```js
const date = new Date( 1660209124 * 1000 );
const dt = date.getFullYear() + '-' + (date.getMonth()+1) + '-' +
           date.getDate() + ' ' +
           date.getHours() + ':' + date.getMinutes() + ':' +
           date.getSeconds();
console.log(dt)
```
```
2022-8-11 9:12:4

```

link_youtube: https://youtu.be/ygW_2JRZz3A
