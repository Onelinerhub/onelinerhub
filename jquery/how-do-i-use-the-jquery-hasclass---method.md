# How do I use the jQuery hasClass() method?
// plain

The jQuery `hasClass()` method is used to check if an element has a specific class. It returns a Boolean value of `true` or `false`, depending on whether the element has the specified class.

## Example code

```
if ($('div').hasClass('myClass')) {
  console.log('Element has class');
}
```

## Output example

```
Element has class
```

The code above checks if a `div` element has the class `myClass`. If it does, the message `Element has class` is logged in the console.

The syntax of the `hasClass()` method is as follows:

```
$(selector).hasClass(classname)
```

- `selector` is the element to check for the class name.
- `classname` is the class name to search for.

For more information, see the [jQuery documentation](https://api.jquery.com/hasclass/).

onelinerhub: [How do I use the jQuery hasClass() method?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-hasclass---method)