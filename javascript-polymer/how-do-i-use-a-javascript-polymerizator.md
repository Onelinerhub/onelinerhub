# How do I use a JavaScript Polymerizator?
// plain

A JavaScript Polymerizator is a tool that can be used to combine multiple JavaScript files into one. It is useful for reducing the number of requests a web page needs to make, and can help speed up page loading times.

## Example code

```
var Polymerizator = require('polymerizator');

var polymerizator = new Polymerizator({
  src: './src',
  dest: './dist'
});

polymerizator.build();
```

This example code will take all the JavaScript files located in the `./src` directory, and combine them into a single file located in the `./dist` directory.

The code works in the following way:

1. `var Polymerizator = require('polymerizator')`: this line imports the Polymerizator library from the `polymerizator` module.
2. `var polymerizator = new Polymerizator({...})`: this line creates a new instance of the Polymerizator class, and passes in configuration options.
3. `polymerizator.build()`: this line calls the `build` function on the Polymerizator instance, which will combine all the JavaScript files located in the `src` directory into a single file located in the `dest` directory.

For more information, please refer to the [Polymerizator documentation](https://github.com/polymerizator/polymerizator).

onelinerhub: [How do I use a JavaScript Polymerizator?](https://onelinerhub.com/javascript-polymer/how-do-i-use-a-javascript-polymerizator)