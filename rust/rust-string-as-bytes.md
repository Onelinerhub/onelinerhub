# rust string as bytes
// plain

A Rust `String` can be converted to a `Vec<u8>` of bytes using the `as_bytes()` method. This method returns a `&[u8]` slice, which can be converted to a `Vec<u8>` using the `to_vec()` method.

## Example

```rust
let my_string = String::from("Hello World!");
let bytes = my_string.as_bytes().to_vec();
```

## Output example

```
[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
```

## Code explanation

- `my_string`: a `String` containing the text "Hello World!"
- `as_bytes()`: a method that returns a `&[u8]` slice of the bytes of the `String`
- `to_vec()`: a method that converts a `&[u8]` slice to a `Vec<u8>`

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Slices](https://doc.rust-lang.org/std/primitive.slice.html)