# How to get current time

```js
const time = new Date().toLocaleTimeString('en-gb');

```

- `new Date()` - creates new object to work with dates based on current time (if empty constructor)
- `toLocaleTimeString` - returns locally formatted time string
- `'en-gb'` - locale to use

group: date

## Example: 
```js
const time = new Date().toLocaleTimeString('en-gb');
console.log(time);
```
```
09:32:48

```

link_youtube: https://youtu.be/uh2_VfR72_g
