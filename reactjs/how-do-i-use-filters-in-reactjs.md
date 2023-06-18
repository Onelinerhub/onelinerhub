# How do I use filters in ReactJS?
// plain

Filters in ReactJS are used to manipulate data and render the desired output. To use filters in ReactJS, you need to create a function that takes the data as an argument, and then use the `.filter()` method to filter the data based on the criteria you specify.

For example, let's say you have an array of objects that contains objects with a `name` and `age` property. You can use the `.filter()` method to filter out objects that don't meet the criteria you specify:

```
const people = [
  {name: 'John', age: 30},
  {name: 'Jane', age: 20},
  {name: 'Bob', age: 40},
];

const filteredPeople = people.filter(person => person.age > 30);

console.log(filteredPeople);
// [{name: 'Bob', age: 40}]
```

In the example above, the `.filter()` method takes a callback function that returns a boolean value. The callback function takes a single argument (in this case, `person`), which is the current object being iterated over in the array. The `.filter()` method will then return an array of objects that meet the criteria specified in the callback function (in this case, objects with an `age` property greater than 30).

In addition to the `.filter()` method, you can also use the `Array.prototype.map()` method to filter data. The `.map()` method takes a callback function as its argument and returns a new array with the results of the callback function applied to each element in the original array.

## Helpful links
- [MDN - Array.prototype.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- [MDN - Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

onelinerhub: [How do I use filters in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-filters-in-reactjs)