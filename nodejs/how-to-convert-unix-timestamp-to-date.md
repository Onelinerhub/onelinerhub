# How to convert unix timestamp to date

```js
const date = (new Date( 1660209124 * 1000 )).getDate();
```

- `new Date` - create date/time management object
- `1660209124` - sample timestamp to convert to date
- `* 1000` - convert given timestamp from seconds to milliseconds

group: timestamp

## Example: 
```js
const date = (new Date( 1660209124 * 1000 )).getDate();
console.log(date);
```
```
11

```

