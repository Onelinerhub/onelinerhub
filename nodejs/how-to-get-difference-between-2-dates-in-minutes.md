# How to get difference between 2 dates in minutes

```js
const date1 = new Date("08/05/2022 23:41:20");
const date2 = new Date("08/06/2022 02:56:32");

const diff = date2.getTime() - date1.getTime();
const minutes = Math.ceil(diff / (1000 * 60));
```

- `new Date(` - creates new object to work with dates based on given date/time string
- `const diff` - difference in timestamp between 2 timestamps
- `diff / (1000 * 60)` - convert milliseconds to minutes
- `minutes` - will contain number of minutes between `date1` and `date2`

group: date

## Example: 
```js
const date1 = new Date("08/05/2022 23:41:20");
const date2 = new Date("08/06/2022 02:56:32");

const diff = date2.getTime() - date1.getTime();
const minutes = Math.ceil(diff / (1000 * 60));
console.log( minutes );
```
```
196

```

