# rust string builder
// plain

Rust String Builder is a library that provides a convenient way to build strings in Rust. It provides a `StringBuilder` type that allows you to easily add strings, characters, and other types of data to a string.

## Example code

```rust
let mut sb = StringBuilder::new();
sb.push_str("Hello");
sb.push(' ');
sb.push_str("World!");
let s = sb.build();
```

## Output example

```
Hello World!
```

## Code explanation

- `StringBuilder::new()`: Creates a new `StringBuilder` instance.
- `sb.push_str(string)`: Adds a string to the `StringBuilder`.
- `sb.push(char)`: Adds a character to the `StringBuilder`.
- `sb.build()`: Returns the built string.

## Helpful links
- [Rust String Builder Documentation](https://docs.rs/string-builder/0.1.1/string_builder/)