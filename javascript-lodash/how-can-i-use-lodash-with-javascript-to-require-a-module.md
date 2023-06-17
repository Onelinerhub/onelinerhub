# How can I use Lodash with JavaScript to require a module?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used with JavaScript to require a module by using the `require()` function. The `require()` function takes a module path as an argument and returns the module's exports. For example:

```
// my-module.js
module.exports = {
  sayHello: function() {
    console.log('Hello!');
  }
};

// main.js
const myModule = require('./my-module');
myModule.sayHello();
// Output: Hello!
```

In this example, the `require()` function is used to import the `my-module.js` module into the `main.js` file. The `myModule` variable is assigned the return value of `require()`, which is the module's exports object. The `sayHello()` function is then called on the `myModule` object, which prints the string `Hello!` to the console.

## Code explanation


1. `module.exports = { ... }`: This is used to export the `sayHello()` function from the `my-module.js` module.
2. `const myModule = require('./my-module')`: This is used to import the `my-module.js` module into the `main.js` file, and assign the module's exports to the `myModule` variable.
3. `myModule.sayHello()`: This is used to call the `sayHello()` function on the `myModule` object.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/4.17.15)
- [Node.js require() Documentation](https://nodejs.org/api/modules.html#modules_require)

onelinerhub: [How can I use Lodash with JavaScript to require a module?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-with-javascript-to-require-a-module)