# How can I use Lodash to find a property in a nested object in JavaScript?
// plain

Lodash is a JavaScript library that provides utility functions for common programming tasks. It can be used to find a property in a nested object in JavaScript. The _.get() function is used to do this. It takes an object and a path as arguments and returns the value of the property at the given path.

## Example


```
const obj = {
  a: {
    b: {
      c: 'value'
    }
  }
};

console.log(_.get(obj, 'a.b.c'));
```

## Output example

```
value
```

The code above will get the value of the property at `a.b.c` in the `obj` object. The `_.get()` function takes two arguments:

1. Object - The object to query.
2. Path - The path of the property to get.

## Helpful links

- [Lodash Documentation](https://lodash.com/docs/)
- [_.get() Documentation](https://lodash.com/docs/4.17.15#get)

onelinerhub: [How can I use Lodash to find a property in a nested object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-find-a-property-in-a-nested-object-in-javascript)