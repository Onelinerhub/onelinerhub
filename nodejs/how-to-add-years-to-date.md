# How to add years to date

```js
let dt = new Date();
dt.setFullYear(dt.getFullYear() + 5);

```

- `new Date` - create date/time management object
- `.setFullYear(` - sets year for the given date object
- `getFullYear()` - returns year of the date
- `dt.getFullYear() + 5` - adds 5 years to the given date
- `5` - number of months to add

group: date

## Example: 
```js
let dt = new Date();
console.log(dt.toLocaleDateString("en-gb"))

dt.setFullYear(dt.getFullYear() + 5);
console.log(dt.toLocaleDateString("en-gb"))
```
```
11/08/2022
11/08/2027

```

