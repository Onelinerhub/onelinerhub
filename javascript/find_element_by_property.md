# Search array of objects by property value

```javascript
var arr = [{a: 1}, {a: 2}, {a: 3}];
var obj = arr.find(obj => obj.a === 2);
```

- var arr - declare test array of objects to search
- var obj - will contain found object
- arr.find - finds array element by a specified rule
- obj => obj.a === 2 - we ask to select object with ```a``` property equals to ```2```
