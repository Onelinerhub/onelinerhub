# How to compare boxed in Rust
// plain

Comparing boxed values in Rust is done using the `PartialEq` trait. This trait provides the `eq` method which can be used to compare two boxed values.

Example code:
```rust
let a = Box::new(5);
let b = Box::new(5);

assert!(a == b);
```

Output:
```
assertion successful
```

The code above creates two boxed values `a` and `b` and then uses the `eq` method to compare them. If the values are equal, the assertion is successful.

Code parts:
- `Box::new(5)`: creates a new boxed value containing the integer `5`
- `a == b`: uses the `eq` method to compare the two boxed values
- `assert!(a == b)`: checks if the two boxed values are equal and prints an assertion successful message if they are

## Helpful links
- [Rust Documentation - PartialEq](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)

group: rust-box