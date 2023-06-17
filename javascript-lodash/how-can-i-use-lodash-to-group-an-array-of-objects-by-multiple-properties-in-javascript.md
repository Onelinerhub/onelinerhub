# How can I use Lodash to group an array of objects by multiple properties in JavaScript?
// plain

Lodash provides a convenient way to group an array of objects by multiple properties in JavaScript. To do this, you can use the _.groupBy() method. The _.groupBy() method takes two arguments: an array of objects and a function that returns the value to group by.

For example, the following code will group an array of objects by their `name` and `age` properties:

```javascript
const people = [
  {name: 'John', age: 25},
  {name: 'Tom', age: 30},
  {name: 'John', age: 20},
  {name: 'Tom', age: 25},
];

const groupedPeople = _.groupBy(people, p => [p.name, p.age]);

console.log(groupedPeople);
/*
## Output example

{
  'John,25': [{name: 'John', age: 25}],
  'Tom,30': [{name: 'Tom', age: 30}],
  'John,20': [{name: 'John', age: 20}],
  'Tom,25': [{name: 'Tom', age: 25}],
}
*/
```

The code above uses the `_.groupBy()` method to group an array of objects by their `name` and `age` properties. The `_.groupBy()` method takes a function as its second argument, which returns the value to group by. In this example, the function returns an array containing both the `name` and `age` properties of each object. The `_.groupBy()` method returns an object with keys corresponding to the values returned by the function, and values corresponding to the objects with those values.

For more information on the _.groupBy() method, see the [Lodash documentation](https://lodash.com/docs/4.17.15#groupBy).

onelinerhub: [How can I use Lodash to group an array of objects by multiple properties in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-group-an-array-of-objects-by-multiple-properties-in-javascript)