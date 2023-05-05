# How do I convert a hex string to bytes in Rust?
// plain

To convert a hex string to bytes in Rust, you can use the `from_hex` method from the `hex` crate. This method takes a `&str` and returns a `Result<Vec<u8>, hex::FromHexError>`.

## Example code

```rust
use hex;

let hex_string = "deadbeef";
let bytes = hex::from_hex(hex_string).unwrap();
```

## Output example

```
[222, 173, 190, 239]
```

## Code explanation

- `use hex;`: imports the `hex` crate
- `let hex_string = "deadbeef";`: creates a `&str` with the hex string
- `let bytes = hex::from_hex(hex_string).unwrap();`: calls the `from_hex` method from the `hex` crate, passing the `&str` as an argument, and unwraps the `Result`

## Helpful links
- [hex crate documentation](https://docs.rs/hex/0.3.2/hex/)