# How to convert a Rust slice of u8 to a string?
// plain

To convert a Rust slice of u8 to a string, you can use the `str::from_utf8` function. This function takes a slice of bytes and returns a `Result<&str, Utf8Error>`.

## Example code

```rust
let bytes = [104, 101, 108, 108, 111];
let string = str::from_utf8(&bytes).unwrap();
```

## Output example

```
hello
```

The code above does the following:

1. `let bytes = [104, 101, 108, 108, 111];` - creates a slice of bytes
2. `let string = str::from_utf8(&bytes).unwrap();` - calls the `str::from_utf8` function with the `&bytes` slice as an argument, and then unwraps the `Result` to get the `&str`

## Helpful links

- [str::from_utf8](https://doc.rust-lang.org/std/str/fn.from_utf8.html) - official documentation for the `str::from_utf8` function

group: rust-slice