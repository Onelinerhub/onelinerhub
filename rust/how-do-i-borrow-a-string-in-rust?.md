# How do I borrow a string in Rust?
// plain

You can borrow a string in Rust by using the `&` operator. This operator creates a reference to the string, allowing you to use the string without taking ownership of it.

For example:
```rust
let s1 = String::from("hello");
let s2 = &s1;
```
This code creates a `String` called `s1` and then creates a reference to it called `s2`.

## Code explanation

- `let s1 = String::from("hello");`: This creates a `String` called `s1` with the value `"hello"`.
- `let s2 = &s1;`: This creates a reference to `s1` called `s2`.

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Strings](https://doc.rust-lang.org/std/string/index.html)