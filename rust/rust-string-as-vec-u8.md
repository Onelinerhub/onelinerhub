# rust string as vec u8
// plain

A `String` in Rust is a UTF-8 encoded, growable array of bytes. It can be converted to a `Vec<u8>` using the `as_bytes()` method. This method returns a `&[u8]` which can be converted to a `Vec<u8>` using the `to_vec()` method.

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


- `let s = String::from("Hello world!");`: This line creates a `String` from the given string literal.

- `let v: Vec<u8> = s.as_bytes().to_vec();`: This line calls the `as_bytes()` method on the `String` to get a `&[u8]` slice, and then calls the `to_vec()` method on the slice to convert it to a `Vec<u8>`.

## Helpful links

- [String](https://doc.rust-lang.org/std/string/struct.String.html)
- [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [as_bytes](https://doc.rust-lang.org/std/string/struct.String.html#method.as_bytes)
- [to_vec](https://doc.rust-lang.org/std/slice/trait.AsRef.html#tymethod.to_vec)