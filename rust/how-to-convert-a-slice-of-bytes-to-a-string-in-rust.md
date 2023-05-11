# How to convert a slice of bytes to a string in Rust?
// plain

To convert a slice of bytes to a string in Rust, you can use the `std::str::from_utf8` function. This function takes a slice of bytes and returns a `Result<&str, Utf8Error>`.

## Example code

```rust
let bytes = [104, 101, 108, 108, 111];
let string = std::str::from_utf8(&bytes).unwrap();
```

## Output example

```
hello
```

The code above does the following:

1. `let bytes = [104, 101, 108, 108, 111];` - creates a byte array containing the ASCII codes for the characters `h`, `e`, `l`, `l`, and `o`.
2. `let string = std::str::from_utf8(&bytes).unwrap();` - calls the `std::str::from_utf8` function with the byte array as an argument, and assigns the result to the `string` variable. The `unwrap` method is used to convert the `Result` into a `&str`.

## Helpful links

- [std::str::from_utf8](https://doc.rust-lang.org/std/str/fn.from_utf8.html)

group: rust-slice