# Rust bytes buffer example
// plain

Rust provides a `Vec<u8>` type to represent a buffer of bytes. This type is a growable array of bytes, and can be used to store data such as images, audio, and text.

```rust
let mut buffer = Vec::new();
buffer.push(0x41);
buffer.push(0x42);
buffer.push(0x43);
```

The above code creates a `Vec<u8>` buffer and adds three bytes to it (0x41, 0x42, and 0x43).

- `let mut buffer = Vec::new();` creates a new empty `Vec<u8>` buffer.
- `buffer.push(0x41);` adds the byte 0x41 to the end of the buffer.
- `buffer.push(0x42);` adds the byte 0x42 to the end of the buffer.
- `buffer.push(0x43);` adds the byte 0x43 to the end of the buffer.

The output of the above code is a `Vec<u8>` buffer containing the bytes 0x41, 0x42, and 0x43.

## Helpful links
- [Rust Vec Documentation](https://doc.rust-lang.org/std/vec/struct.Vec.html)

group: rust-bytes