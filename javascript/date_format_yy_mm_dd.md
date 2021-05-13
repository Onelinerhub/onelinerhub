# Format date in YY/MM/DD

```javascript
var d = new Date();
var formatted = d.getFullYear().toString().substr(-2) + '/' + ('0' + (d.getMonth()+1)).slice(-2) + '/' + ('0' + d.getDate()).slice(-2);
```

- var d = new Date() - create date object
- d.getDate() - returns day of the month
- d.getMonth() - returns month of the year
- d.getFullYear() - returns current year (4 digits)
- formatted - this variable will contain formatted date string

group: date_format
