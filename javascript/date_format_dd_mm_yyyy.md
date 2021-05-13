# Format date in DD.MM.YYYY

```javascript
var d = new Date();
var formatted = ('0' + d.getDate()).slice(-2) + '.' + ('0' + (d.getMonth()+1)).slice(-2) + '.' + d.getFullYear();
```

- var d = new Date() - create date object
- d.getDate() - returns day of the month
- d.getMonth() - returns month of the year
- d.getFullYear() - returns current year (4 digits)

group: date_format
