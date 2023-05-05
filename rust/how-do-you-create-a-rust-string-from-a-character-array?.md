# How do you create a Rust string from a character array?
// plain

Creating a Rust string from a character array can be done using the `String::from_utf8` function. This function takes a `&[u8]` as an argument and returns a `Result<String, FromUtf8Error>`.

## Example code

```rust
let chars: &[u8] = &[104, 101, 108, 108, 111];
let string = String::from_utf8(chars).unwrap();
```

## Output example

```
hello
```

The code above creates a `&[u8]` from the character array `[104, 101, 108, 108, 111]` and passes it to the `String::from_utf8` function. The `unwrap` method is used to convert the `Result<String, FromUtf8Error>` into a `String`.

## Code explanation

- `&[u8]`: A type of array that contains 8-bit unsigned integers.
- `String::from_utf8`: A function that takes a `&[u8]` as an argument and returns a `Result<String, FromUtf8Error>`.
- `unwrap`: A method that converts a `Result<String, FromUtf8Error>` into a `String`.

## Helpful links
- [Rust Documentation - String](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - FromUtf8Error](https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html)