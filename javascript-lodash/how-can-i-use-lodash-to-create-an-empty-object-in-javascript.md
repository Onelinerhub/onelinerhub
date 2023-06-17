# How can I use Lodash to create an empty object in JavaScript?
// plain

Using Lodash to create an empty object in JavaScript is easy and straightforward. To do so, you can use the `_.zipObject` method. This method takes two arrays, one containing keys and the other containing values, and creates an object from them. If you pass in empty arrays, the resulting object will be empty.

## Example code


```
const emptyObject = _.zipObject([], [])
console.log(emptyObject)
```

## Output example


```
{}
```

The code above creates an empty object using Lodash's `_.zipObject` method. It passes two empty arrays as parameters to the method, which returns an empty object.

Parts of code:
- `_.zipObject` - the Lodash method used to create an empty object from two empty arrays.
- `[], []` - two empty arrays passed as parameters to the `_.zipObject` method.

## Helpful links
- [Lodash documentation for _.zipObject](https://lodash.com/docs/4.17.15#zipObject)

onelinerhub: [How can I use Lodash to create an empty object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-create-an-empty-object-in-javascript)