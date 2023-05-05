# How do I get the first character from a string in Rust?
// plain

The easiest way to get the first character from a string in Rust is to use the `chars()` method. This method returns an iterator over the characters of a string. The first character can then be accessed using the `next()` method.

## Example code

```
let s = "Hello";
let first_char = s.chars().next();
```

## Output example

```
Some('H')
```

## Code explanation

- `let s = "Hello"`: This line declares a string variable `s` and assigns it the value `"Hello"`.
- `let first_char = s.chars().next()`: This line calls the `chars()` method on the `s` string variable, which returns an iterator over the characters of the string. The `next()` method is then called on the iterator, which returns the first character of the string.

## Helpful links
- [String](https://doc.rust-lang.org/std/string/struct.String.html)
- [chars()](https://doc.rust-lang.org/std/primitive.str.html#method.chars)
- [next()](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.next)