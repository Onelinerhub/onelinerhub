# rust string contains
// plain

A `String` in Rust is a UTF-8 encoded, growable bit of text. It is a collection of `char`s, and is one of the most commonly used data types in Rust.

```rust
let mut my_string = String::new();
my_string.push_str("Hello, world!");

println!("{}", my_string);
```

## Output example

```
Hello, world!
```

The `String` type has several methods that can be used to check if it contains a certain substring. These include:

- `contains()`: Checks if a `String` contains a given substring.
- `find()`: Returns the index of the first character of a given substring in a `String`.
- `rfind()`: Returns the index of the last character of a given substring in a `String`.

These methods can be used to check if a `String` contains a given substring. For example:

```rust
let my_string = String::from("Hello, world!");

assert!(my_string.contains("world"));
assert_eq!(my_string.find("world"), 7);
assert_eq!(my_string.rfind("world"), 7);
```

The `contains()` method returns a `bool` indicating whether the `String` contains the given substring. The `find()` and `rfind()` methods return the index of the first and last character of the substring, respectively.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#primitive-types)