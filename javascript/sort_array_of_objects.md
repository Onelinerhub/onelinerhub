# Sort array of objects by specific property

```javascript
var arr = [{prop: 3}, {prop: 1}, {prop: 2}];
arr.sort(function(a, b) { return a.prop > b.prop ? 1 : -1; } );
```

- var arr - declares test array of objects to sort
- arr.sort - this function will sort an array by custom callback function and overwrite ```arr``` with sorted array
- function(a, b) - callback will get 2 array elements to compare: ```a``` and ```b```
- a.prop > b.prop ? 1 : -1 - will sort our array in ascending order of ```prop``` values
