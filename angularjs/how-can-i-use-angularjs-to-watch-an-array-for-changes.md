# How can I use AngularJS to watch an array for changes?
// plain

AngularJS provides a `$watch` function for watching an array for changes. This function takes two arguments: the array to watch and a callback function that will be called when the array changes.

```javascript
var arr = [1, 2, 3];
$scope.$watch(arr, function (newArr, oldArr) {
  console.log('Array changed from', oldArr, 'to', newArr);
});

arr.push(4);
// Output: Array changed from [1, 2, 3] to [1, 2, 3, 4]
```

The `$watch` function takes two arguments:
1. The array to watch (`arr` in the example above).
2. A callback function that will be called when the array changes (`function (newArr, oldArr)` in the example above). The callback function takes two arguments: the new array (`newArr`) and the old array (`oldArr`).

In the example code above, the `$watch` function is used to watch the `arr` array. When the `arr.push(4)` statement is executed, the callback function is called and the output `Array changed from [1, 2, 3] to [1, 2, 3, 4]` is displayed.

For more information on the `$watch` function, see the [AngularJS documentation](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$watch).

onelinerhub: [How can I use AngularJS to watch an array for changes?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-watch-an-array-for-changes)