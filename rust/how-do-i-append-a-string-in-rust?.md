# How do I append a string in Rust?
// plain

You can append a string in Rust using the `push_str()` method. This method takes a string slice as an argument and appends it to the end of the string.

## Example code

```
let mut s = String::from("Hello ");
s.push_str("World!");
```

## Output example

```
Hello World!
```

## Code explanation

- `let mut s = String::from("Hello ");`: This line creates a mutable `String` variable `s` and assigns it the value `Hello `.
- `s.push_str("World!");`: This line calls the `push_str()` method on the `s` variable, passing in the string `World!` as an argument. This appends the string `World!` to the end of the `s` variable.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)