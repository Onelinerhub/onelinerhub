# How do I convert a string to a vector of u8 in Rust?
// plain

To convert a string to a vector of u8 in Rust, you can use the `as_bytes()` method on a `String` type. This will return a `&[u8]` type, which can be converted to a `Vec<u8>` using the `to_vec()` method.

## Example code

```rust
let s = String::from("Hello world!");
let v: Vec<u8> = s.as_bytes().to_vec();
```

## Output example

```
[72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
```

## Code explanation

- `let s = String::from("Hello world!");`: creates a `String` type from the string literal `"Hello world!"`
- `let v: Vec<u8> = s.as_bytes().to_vec();`: creates a `Vec<u8>` type from the `&[u8]` type returned by the `as_bytes()` method on the `String` type

## Helpful links
- [String::as_bytes()](https://doc.rust-lang.org/std/string/struct.String.html#method.as_bytes)
- [Vec::to_vec()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.to_vec)