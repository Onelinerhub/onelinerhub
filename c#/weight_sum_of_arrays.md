# How to do weighted sum of two arrays

```C#
var sum = new int[]{10,20,100}.Zip(new int[]{90,10,100}, (v1,v2) => v1 * v2).Sum();
```
- var sum - variable for the weighted array total
- new int[] - initialize an array of values
- .Zip - function that co-process each value on every array elements
- .Sum() - function that retrieves the sum of the array elements