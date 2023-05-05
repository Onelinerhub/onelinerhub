# rust string bytes
// plain

A Rust `String` is a UTF-8 encoded sequence of bytes. It is a collection of `u8` values, and is stored as a vector of bytes (`Vec<u8>`).

```rust
let s = String::from("Hello world!");
let bytes = s.as_bytes();
```

The output of the above code is `[72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]`.

## Code explanation


- `let s = String::from("Hello world!");`: This creates a `String` from the given string literal.
- `let bytes = s.as_bytes();`: This creates a `Vec<u8>` from the `String`, containing the UTF-8 encoded bytes of the string.

## Helpful links

- [The Rust Programming Language - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [The Rust Programming Language - Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#primitive-types)