# How do I find the index of a substring in a string in Rust?
// plain

The `find()` method of the `str` type can be used to find the index of a substring in a string in Rust.

## Example code

```
let s = "Hello World!";
let index = s.find("World");
```

## Output example

```
Some(6)
```

The `find()` method takes a `&str` as an argument and returns an `Option<usize>` which is `Some(index)` if the substring is found, or `None` if it is not found.

## Code explanation

- `let s = "Hello World!";`: This declares a string variable `s` with the value `Hello World!`.
- `let index = s.find("World");`: This calls the `find()` method on the `s` string variable, passing in the substring `World` as an argument.
- `Some(6)`: This is the output of the `find()` method, which is `Some(index)` if the substring is found, or `None` if it is not found. In this case, the substring `World` is found at index 6.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)