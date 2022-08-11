# How to get difference between 2 dates in days

```js
const date1 = new Date("07/01/2022 23:41:20");
const date2 = new Date("08/06/2022 02:56:32");

const diff = date2.getTime() - date1.getTime();
const days = Math.ceil(diff / (1000 * 60*60*24));
```

- `new Date(` - creates new object to work with dates based on given date/time string
- `const diff` - difference in timestamp between 2 timestamps
- `diff / (1000 * 60*60*24)` - convert milliseconds to days
- `days` - will contain number of days between `date` and `date2`

group: date

## Example: 
```js
const date1 = new Date("07/01/2022 23:41:20");
const date2 = new Date("08/06/2022 02:56:32");

const diff = date2.getTime() - date1.getTime();
const days = Math.ceil(diff / (1000 * 60*60*24));
console.log( days );
```
```
36

```

