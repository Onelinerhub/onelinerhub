# How do I install JavaScript Lodash?
// plain

To install Lodash, you need to have Node.js installed. Lodash is a JavaScript library that provides utility functions for common programming tasks.

1. Install Node.js:

First, you need to install [Node.js](https://nodejs.org/en/download/) on your computer.

2. Install Lodash:

Once Node.js is installed, you can use npm (Node Package Manager) to install Lodash. To install Lodash, open a command terminal and type the following command:

```
npm install lodash
```

3. Import Lodash:

You can import Lodash into your project by using the following code:

```
const _ = require('lodash');
```

4. Use Lodash:

You can now use Lodash in your project. For example, you can use the [`_.map()`](https://lodash.com/docs/4.17.15#map) function to map an array of numbers to their squares:

```
const numbers = [1,2,3,4,5];
const squares = _.map(numbers, n => n * n);
console.log(squares);
```

## Output example

```
[ 1, 4, 9, 16, 25 ]
```

Once you have installed Lodash, you can use its many utility functions to make your code simpler and more efficient.

onelinerhub: [How do I install JavaScript Lodash?](https://onelinerhub.com/javascript-lodash/how-do-i-install-javascript-lodash)