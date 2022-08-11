# How to add days to date

```js
let dt = new Date();
dt.setDate(dt.getDate() + 25);

```

- `new Date` - create date/time management object
- `.setDate(` - set days for the given date object
- `getDate()` - returns days (number of a day in week)
- `dt.getDate() + 25` - adds 25 days to the given date

group: date

## Example: 
```js
let dt = new Date();
console.log(dt.toLocaleDateString("en-gb"))

dt.setDate(dt.getDate() + 25);
console.log(dt.toLocaleDateString("en-gb"))
```
```
11/08/2022
05/09/2022

```

