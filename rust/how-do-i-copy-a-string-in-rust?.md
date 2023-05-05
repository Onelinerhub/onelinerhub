# How do I copy a string in Rust?
// plain

Copying a string in Rust is done using the `to_owned()` method. This method creates a new owned string from a string slice.

## Example code

```
let s = "Hello World";
let s_copy = s.to_owned();
```

## Output example

```
Hello World
```

The `to_owned()` method takes a string slice and creates a new owned string from it. The new string is a deep copy of the original string, meaning that any changes made to the new string will not affect the original string.

## Code explanation

- `let s = "Hello World";`: This line creates a string literal and assigns it to the variable `s`.
- `let s_copy = s.to_owned();`: This line creates a new owned string from the string slice `s` and assigns it to the variable `s_copy`.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)