# How to add months to date

```js
let dt = new Date();
dt.setMonth(dt.getMonth() + 4);

```

- `new Date` - create date/time management object
- `.setMonth(` - sets months for the given date object
- `getMonth()` - returns months of the date
- `dt.getMonth() + 4` - adds 4 months to the given date
- `4` - number of months to add

group: date

## Example: 
```js
let dt = new Date();
console.log(dt.toLocaleDateString("en-gb"))

dt.setMonth(dt.getMonth() + 4);
console.log(dt.toLocaleDateString("en-gb"))
```
```
11/08/2022
11/12/2022

```

