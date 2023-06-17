# How can I use Lodash's throttle function in JavaScript?
// plain

The `throttle` function in Lodash is a powerful utility for controlling the rate of execution of a given function. It can be used to limit the number of times a function is called in a given period of time.

## Example code

```javascript
// Setup the throttled function
const throttledFunction = _.throttle(function() {
  console.log('Function called!');
}, 1000); // 1 second

// Call the function multiple times
throttledFunction();
throttledFunction();
throttledFunction();

// Output:
// Function called!
```

The code above will call the function once, after 1 second has elapsed. The other calls will be ignored.

The `_.throttle` function takes two parameters:

1. The function to be throttled
2. The delay in milliseconds

It also accepts an optional third parameter, which is an object with two properties: `leading` and `trailing`. These determine whether the function should be called once immediately, and then throttled, or if the function should be called after the delay. The default is to call the function immediately and then throttle.

## Helpful links

- [Lodash Documentation - throttle](https://lodash.com/docs/4.17.15#throttle)
- [MDN - Throttle Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/throttle)

onelinerhub: [How can I use Lodash's throttle function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-s-throttle-function-in-javascript)