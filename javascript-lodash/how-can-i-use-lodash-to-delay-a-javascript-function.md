# How can I use Lodash to delay a JavaScript function?
// plain

Using Lodash, you can delay the execution of a JavaScript function with the `_.delay()` function. The syntax for this is:

```
_.delay(function, wait, [arg1], [arg2], ...)
```

Where `function` is the function to be delayed, `wait` is the amount of time (in milliseconds) to wait before executing the function, and `[arg1], [arg2], ...` are optional arguments to be passed to the function.

For example, the following code will log "Hello World!" after a delay of 500 milliseconds:

```
_.delay(function() {
  console.log('Hello World!');
}, 500);
```

## Output example


```
Hello World!
```

## Code explanation


1. `_.delay()` - the Lodash function used to delay the execution of a function
2. `function` - the function to be delayed
3. `wait` - the amount of time (in milliseconds) to wait before executing the function
4. `[arg1], [arg2], ...` - optional arguments to be passed to the function

## Helpful links

- [Lodash Documentation - _.delay()](https://lodash.com/docs/4.17.15#delay)
- [MDN Documentation - setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)

onelinerhub: [How can I use Lodash to delay a JavaScript function?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-delay-a-javascript-function)