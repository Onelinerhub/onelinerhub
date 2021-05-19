# Shuffle (randomize) an array

```javascript
var arr = [1, 2, 3, 4, 5];
for ( var i = arr.length - 1; i > 0; i-- ) {
  var rand = Math.round(Math.random() * i);
  [arr[i], arr[rand]] = [arr[rand], arr[i]];
}
```

- var arr - declare test array to randomize
- Math.round(Math.random() * i) - pick random index
- \[arr\[i\], arr\[rand\]\] = \[arr\[rand\], arr\[i\]\] - swap values between current (```i```) and random (```rand```) position
