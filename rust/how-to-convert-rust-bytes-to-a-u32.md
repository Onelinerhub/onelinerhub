# How to convert Rust bytes to a u32?
// plain

To convert Rust bytes to a u32, you can use the `from_be_bytes` method from the `std::convert::TryInto` trait. This method takes a slice of bytes and returns a `Result` containing either the converted value or an error.

## Example code

```rust
let bytes = [0x00, 0x00, 0x00, 0x2A];
let value = u32::from_be_bytes(bytes);
assert_eq!(value, 42);
```
## Output example

```
assertion successful
```

## Code explanation

- `let bytes = [0x00, 0x00, 0x00, 0x2A];`: This line creates a byte array containing the bytes to be converted.
- `let value = u32::from_be_bytes(bytes);`: This line calls the `from_be_bytes` method on the `u32` type, passing in the byte array as an argument.
- `assert_eq!(value, 42);`: This line uses the `assert_eq!` macro to check that the value returned by the `from_be_bytes` method is equal to the expected value (in this case, 42).

## Helpful links
- [std::convert::TryInto](https://doc.rust-lang.org/std/convert/trait.TryInto.html)
- [assert_eq!](https://doc.rust-lang.org/std/macro.assert_eq.html)

group: rust-bytes