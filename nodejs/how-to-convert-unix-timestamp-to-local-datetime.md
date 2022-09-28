# How to convert unix timestamp to local date/time

```js
const date = new Date( 1660209124 * 1000 );
const dt = date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
```

- `new Date` - create date/time management object
- `1660209124` - sample timestamp to convert to date
- `* 1000` - convert given timestamp from seconds to milliseconds
- `toLocaleDateString` - returns locally formatted date string
- `toLocaleTimeString` - returns locally formatted time string

group: timestamp

## Example: 
```js
const date = new Date( 1660209124 * 1000 );
const dt = date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
console.log(dt)
```
```
8/11/2022 9:12:04 AM

```

link_youtube: https://youtu.be/fhun88cvx7I
