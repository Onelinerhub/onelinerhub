# How do I use the lodash get function in JavaScript?
// plain

The `_.get()` function in Lodash is used to retrieve a value from an object given a path. It is a safe way to access a property of an object, as it will return `undefined` if the path does not exist instead of throwing an error.

## Example code

```
const object = {
  a: {
    b: {
      c: 'value'
    }
  }
};

const value = _.get(object, 'a.b.c');

console.log(value);
```

## Output example

```
value
```

The code above uses the `_.get()` function to retrieve the value of `'a.b.c'` from the `object` variable. The `_.get()` function takes two parameters, the object and the path. The path is a string that is used to access the value. In this case, `'a.b.c'` is the path and `value` is the value that is returned.

## Code explanation

- `const object`: Declares a variable named `object` and assigns it a value.
- `const value = _.get(object, 'a.b.c')`: Uses the `_.get()` function to retrieve the value of `'a.b.c'` from the `object` variable and assigns it to the `value` variable.
- `console.log(value)`: Logs the value of the `value` variable to the console.

## Helpful links
- [Lodash Documentation - _.get()](https://lodash.com/docs/4.17.15#get)

onelinerhub: [How do I use the lodash get function in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-the-lodash-get-function-in-javascript)