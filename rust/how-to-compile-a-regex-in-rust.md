# How to compile a regex in Rust?
// plain

Compiling a regex in Rust is a simple process. It can be done using the `regex!` macro. This macro takes a string literal containing the regular expression and returns a `Regex` object.

```rust
let re = regex!(r"^\d{4}-\d{2}-\d{2}$");
```

The `regex!` macro takes the following parts:

- `r`: A raw string literal prefix. This tells the compiler to interpret the string as a regular expression instead of a normal string.
- The regular expression itself: `^\d{4}-\d{2}-\d{2}$`

The output of the example code is a `Regex` object that can be used to match strings against the regular expression.

## Helpful links

- [The Rust Programming Language - Regular Expressions](https://doc.rust-lang.org/book/ch19-06-regular-expressions.html)
- [The Rust Reference - regex!](https://doc.rust-lang.org/reference/macros-by-example.html#regex)

group: rust-regex

onelinerhub: [How to compile a regex in Rust?](https://onelinerhub.com/rust/how-to-compile-a-regex-in-rust)