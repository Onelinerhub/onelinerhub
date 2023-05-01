# How to join bytes in Rust
// plain

Joining bytes in Rust can be done using the `concat()` method from the `std::vec` module. This method takes a vector of bytes and returns a single byte vector containing all the bytes from the original vector.

## Code example:
```
use std::vec;

let bytes1 = vec![0x01, 0x02, 0x03];
let bytes2 = vec![0x04, 0x05, 0x06];

let joined_bytes = vec::concat(vec![bytes1, bytes2]);

println!("{:?}", joined_bytes);
```

### Output
`[1, 2, 3, 4, 5, 6]`

Explanation:
- `use std::vec`: imports the `vec` module from the `std` library
- `let bytes1 = vec![0x01, 0x02, 0x03]`: creates a vector of bytes containing the values `0x01`, `0x02`, and `0x03`
- `let bytes2 = vec![0x04, 0x05, 0x06]`: creates a vector of bytes containing the values `0x04`, `0x05`, and `0x06`
- `let joined_bytes = vec::concat(vec![bytes1, bytes2])`: calls the `concat()` method from the `vec` module, passing in a vector containing the two byte vectors `bytes1` and `bytes2`
- `println!("{:?}", joined_bytes)`: prints the joined bytes vector

## Helpful links:
- [Rust Documentation - Vec::concat()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.concat)
- [Rust By Example - Vectors](https://doc.rust-lang.org/rust-by-example/vectors.html)