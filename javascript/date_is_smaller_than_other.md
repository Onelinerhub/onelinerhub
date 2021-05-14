# How to check if one date is in past compared to another

```javascript
var d1 = new Date('2021-11-11');
var d2 = new Date('2022-12-12');
var is_in_past = d1 < d2;
```

- var d1 - first date
- var d2 - second date
- is_in_past - will contain ```true``` if first date ```d1``` is in past compared to second ```d2```
- d1 < d2 - we can compare dates with standard ```>``` operator

group: compare_dates
