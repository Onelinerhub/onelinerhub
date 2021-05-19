# Extract certain object properties values as array from array of objects

```javascript
var arr = [{a: 1}, {a: 2}, {a: 3}];
var props = arr.map(el => el.a);
```

- var arr - declare test object array
- props - array will contain array of selected properties values
- arr.map(el => el.a) - build an array of ```a``` properties of objects in ```arr``` array
