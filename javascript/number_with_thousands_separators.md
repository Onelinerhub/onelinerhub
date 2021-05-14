# Format number thousands separators

```javascript
var num = 1234567;
num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
```

- var num - declare test number
- num.toString() - converts number to string
- replace - regex to replace every 3 symbols to a given character ([source](https://stackoverflow.com/questions/2901102/how-to-print-a-number-with-commas-as-thousands-separators-in-javascript))
- ' ' - character to separate thousands (space in our example)
