# How to get format date in "yyyy-mm-dd"

```js
const d = new Date("10/07/2022").toLocaleDateString("en-gb").split('/');
const date = d[2] + '-' + d[0] + '-' + d[1];
```

- `new Date("10/07/2022")` - create date object with given date
- `toLocaleDateString` - returns locally formatted date string
- `"en-gb"` - use this locale to get date in `m/d/y` format
- `d[2] + '-' + d[0] + '-' + d[1]` - assemble date components to single string
- `date` - will contain date in `YYYY-MM-DD` format

group: date

## Example: 
```js
const d = new Date("10/07/2022").toLocaleDateString("en-gb").split('/');
const date = d[2] + '-' + d[0] + '-' + d[1];
console.log(date);
```
```
2022-07-10

```

