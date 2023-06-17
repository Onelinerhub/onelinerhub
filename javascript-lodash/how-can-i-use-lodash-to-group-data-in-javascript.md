# How can I use Lodash to group data in JavaScript?
// plain

Lodash is a JavaScript library that can be used to group data. The method that can be used is the _.groupBy() function. This function takes an array of objects and groups them based on the property specified.

For example:
```
const data = [
  {name: 'John', age: 30},
  {name: 'Mary', age: 25},
  {name: 'Michael', age: 30},
  {name: 'Steve', age: 25},
];

const groupedData = _.groupBy(data, 'age');
console.log(groupedData);
```

## Output example

```
{
  25: [
    {name: 'Mary', age: 25},
    {name: 'Steve', age: 25}
  ],
  30: [
    {name: 'John', age: 30},
    {name: 'Michael', age: 30}
  ]
}
```

The code above uses the _.groupBy() function to group the data array based on the age property. The output is an object with the age as the key and an array of objects for each age.

Parts of the code:
- `const data`: creates a constant variable which holds an array of objects
- `const groupedData = _.groupBy(data, 'age')`: creates a new constant variable and uses the _.groupBy() function to group the data array based on the age property
- `console.log(groupedData)`: logs the grouped data to the console

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [_.groupBy() Documentation](https://lodash.com/docs/4.17.15#groupBy)

onelinerhub: [How can I use Lodash to group data in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-group-data-in-javascript)