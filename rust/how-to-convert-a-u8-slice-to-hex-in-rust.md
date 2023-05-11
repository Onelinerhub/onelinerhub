# How to convert a u8 slice to hex in Rust?
// plain

To convert a u8 slice to hex in Rust, you can use the `encode_hex` method from the `hex` crate. This method takes a `&[u8]` as an argument and returns a `String` containing the hexadecimal representation of the slice.

## Example code

```rust
use hex::encode_hex;

let bytes = [0x41, 0x42, 0x43];
let hex = encode_hex(&bytes);

println!("{}", hex);
```

## Output example

```
414243
```

## Code explanation

- `use hex::encode_hex;`: imports the `encode_hex` method from the `hex` crate.
- `let bytes = [0x41, 0x42, 0x43];`: creates a `u8` slice containing the bytes `0x41`, `0x42` and `0x43`.
- `let hex = encode_hex(&bytes);`: calls the `encode_hex` method with the `bytes` slice as an argument and stores the result in the `hex` variable.
- `println!("{}", hex);`: prints the `hex` variable to the console.

## Helpful links
- [hex crate documentation](https://docs.rs/hex/0.3.2/hex/)

group: rust-slice