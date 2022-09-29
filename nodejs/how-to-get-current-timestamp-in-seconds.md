# How to get current timestamp in seconds

```js
const ts = Math.round(Date.now() / 1000);
```

- `Date.now()` - return current timestamp in milliseconds
- `Math.round(Date.now() / 1000)` - convert milliseconds to seconds

group: timestamp

## Example: 
```js
const ts = Math.round(Date.now() / 1000);
console.log(ts);
```
```
1660209124

```

link_youtube: https://youtu.be/ZSiEaWriqvM
