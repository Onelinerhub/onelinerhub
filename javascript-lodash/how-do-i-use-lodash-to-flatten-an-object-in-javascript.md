# How do I use Lodash to flatten an object in JavaScript?
// plain

Lodash is a library of JavaScript functions that provides utility functions for common programming tasks. One of the functions it provides is the _.flatten() function, which can be used to flatten an object in JavaScript.

Here is an example of how to use the _.flatten() function:

```
const _ = require('lodash');
const obj = {
  a: {
    b: {
      c: 'd'
    }
  }
};

const flattened = _.flatten(obj);
console.log(flattened);
```

The output of the above code will be:

```
[ 'd' ]
```

The code can be broken down as follows:

1. We import the lodash library into our code using the require() function.
2. We create an object with nested properties.
3. We use the _.flatten() function to flatten the object.
4. We log the result of the _.flatten() function to the console.

For more information on the _.flatten() function, please see the [Lodash documentation](https://lodash.com/docs/4.17.15#flatten).

onelinerhub: [How do I use Lodash to flatten an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-to-flatten-an-object-in-javascript)