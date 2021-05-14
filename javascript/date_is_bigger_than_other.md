# How to check if one date is in future compared to another

```javascript
var d1 = new Date('2021-11-11');
var d2 = new Date('2022-12-12');
var is_in_future = d2 > d1;
```

- var d1 - first date
- var d2 - second date
- is_in_future - will contain ```true``` if second date ```d2``` is in future compared to first ```d1```
- d2 > d1 - we can compare dates with standard ```>``` operator

group: compare_dates
