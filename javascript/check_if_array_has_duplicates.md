# Check if array has a duplicate value

```javascript
var duplicates = new Set(arr).size !== arr.length;
```

- var duplicates - will contain `true` if `arr` array has any duplicate values
- new Set(arr) - form a set with values of the array. A set is an javascript object that has only non-duplicate values
- !== arr.length - If size of the newly formed set is equal to size of the array, you don't have any duplicates, returns `false` else returns `true`
