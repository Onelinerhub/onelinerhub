# How to iterate through object properties

```javascript
for (var prop in obj) {
  if ( Object.prototype.hasOwnProperty.call(obj, prop) ) {
    console.log(prop + ': ' + obj[prop]);
  }
}
```

- for (var prop in obj) - cycle to iterate every ```obj``` object property
- Object.prototype.hasOwnProperty.call - this will exclude possible native properties of an object
- console.log(prop + ': ' + obj[prop]) - replace with your code to operate over ```obj``` properties
