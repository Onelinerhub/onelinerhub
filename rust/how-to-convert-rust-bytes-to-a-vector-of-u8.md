# How to convert Rust bytes to a vector of u8?
// plain

To convert Rust bytes to a vector of u8, you can use the `to_vec()` method. This method will return a `Vec<u8>` from a `&[u8]` or `&mut [u8]`.

## Example code

```rust
let bytes = b"Hello World";
let vec = bytes.to_vec();
```

## Output example

```
[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
```

## Code explanation

- `let bytes = b"Hello World";`: This line creates a byte array containing the string "Hello World".
- `let vec = bytes.to_vec();`: This line calls the `to_vec()` method on the `bytes` array, which returns a `Vec<u8>` containing the same data as the `bytes` array.

## Helpful links
- [Rust Documentation - Primitive Types](https://doc.rust-lang.org/stable/std/primitive.bytes.html)
- [Rust Documentation - Vec](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html)

group: rust-bytes