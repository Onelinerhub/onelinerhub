# How to convert unix timestamp to date

```js
const date = new Date( 1660209124 * 1000 );
const dt = date.getFullYear() + '-' + (date.getMonth()+1) + '-' + date.getDate();
```

- `new Date` - create date/time management object
- `1660209124` - sample timestamp to convert to date
- `* 1000` - convert given timestamp from seconds to milliseconds
- `getFullYear()` - returns year from given date
- `getMonth()` - returns month
- `getDate()` - returns date

group: timestamp

## Example: 
```js
const date = new Date( 1660209124 * 1000 );
const dt = date.getFullYear() + '-' + (date.getMonth()+1) + '-' + date.getDate();
console.log(dt);
```
```
2022-8-11

```

