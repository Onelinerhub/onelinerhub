# How to borrow a string in Rust
// plain

Rust provides a way to borrow a string using the `&` operator. This operator allows you to borrow a string without taking ownership of it.

Example:
```
let s1 = String::from("hello");
let s2 = &s1;
```

The output of the example code is:
```
No output
```

The ## Code explanation

- `let s1 = String::from("hello");`: This line creates a `String` object with the value `hello`.
- `let s2 = &s1;`: This line creates a reference to the `String` object `s1` and assigns it to `s2`.

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Strings](https://doc.rust-lang.org/std/string/index.html)

group: rust-borrow