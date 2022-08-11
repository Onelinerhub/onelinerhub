# How to get convert date to timestamp

```js
const ts = new Date("10/07/2022").getTime();
console.log(ts);
```

- `new Date("10/07/2022")` - create date object with given date
- `getTime()` - returns timestamp in **milliseconds**

group: date

## Example: 
```js
const ts = new Date("10/07/2022").getTime();
console.log(ts);
```
```
1665100800000

```

