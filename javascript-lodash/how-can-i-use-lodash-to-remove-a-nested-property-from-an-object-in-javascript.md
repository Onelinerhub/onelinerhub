# How can I use Lodash to remove a nested property from an object in JavaScript?
// plain

[Lodash](https://lodash.com/) is a popular JavaScript library used for manipulating and working with objects. It provides a range of methods for manipulating objects, including methods for removing nested properties.

The `_.unset()` method can be used to remove a nested property from an object. It takes two arguments: the object and a path to the nested property.

For example, given the following object:

```
const obj = {
  a: {
    b: {
      c: 'hello'
    }
  }
};
```

We can use `_.unset()` to remove the nested property `c`:

```
_.unset(obj, 'a.b.c');
```

This will result in the following object:

```
{
  a: {
    b: {}
  }
}
```

The `_.unset()` method is useful for removing nested properties from an object. It takes two arguments: the object and the path to the nested property. It returns the object with the nested property removed.

## Helpful links

- [Lodash Documentation for `_.unset()`](https://lodash.com/docs/4.17.15#unset)

onelinerhub: [How can I use Lodash to remove a nested property from an object in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-remove-a-nested-property-from-an-object-in-javascript)