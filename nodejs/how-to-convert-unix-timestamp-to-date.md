# How to convert unix timestamp to date

```js
const date = (new Date( 1660209124 * 1000 )).getDate();
```

- `Date.now()` - return current timestamp in milliseconds
- `Math.round(Date.now() / 1000)` - convert milliseconds to seconds

group: timestamp

## Example: 
```js
const date = (new Date( 1660209124 * 1000 )).getDate();
console.log(date);
```
```
1660209124

```

