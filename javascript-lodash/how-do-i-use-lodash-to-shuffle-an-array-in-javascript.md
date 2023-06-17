# How do I use Lodash to shuffle an array in JavaScript?
// plain

Using [Lodash](https://lodash.com/) to shuffle an array in JavaScript is a simple process. First, import the library:

```javascript
const _ = require('lodash');
```

Then, create an array:

```javascript
const arr = [1, 2, 3, 4, 5];
```

Finally, use the `shuffle` method to shuffle the array:

```javascript
const shuffledArr = _.shuffle(arr);
// [4, 5, 1, 3, 2]
```

The `shuffle` method takes the array and returns a shuffled version of it.

- `require('lodash')`: imports the Lodash library
- `_.shuffle(arr)`: takes the array `arr` and returns a shuffled version of it

## Helpful links
- [Lodash Documentation](https://lodash.com/docs/)

onelinerhub: [How do I use Lodash to shuffle an array in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-shuffle-an-array-in-javascript)