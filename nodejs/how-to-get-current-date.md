# How to get current date

```js
const date = new Date().toLocaleDateString('en-us');

```

- `new Date()` - creates new object to work with dates based on current time (if empty constructor)
- `toLocaleDateString` - returns locally formatted date string
- `'en-us'` - locale to use

group: date

## Example: 
```js
const now = new Date().toLocaleDateString('en-us');
console.log(now);
```
```
8/11/2022

```

