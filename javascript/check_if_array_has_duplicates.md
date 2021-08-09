# Check if array has a duplicate value

```javascript
function hasArrayDuplicates(array) {
  return new Set(array).size !== array.length;
}
```

- new Set(array) - form a set with values of the array. A set is an javascript object that has only non-duplicate values
- (new Set(array)).size !== array.length - If size of the newly formed set is equal to size of the array, you don't have any duplicates, returns false else returns true
