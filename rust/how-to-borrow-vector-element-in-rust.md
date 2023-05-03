# How to borrow vector element in Rust
// plain

Rust provides a convenient way to borrow vector elements using the `get` method. This method returns an `Option` type which can be used to check if the element exists.

```rust
let v = vec![1, 2, 3];
let first = v.get(0);
println!("The first element is {:?}", first);
```

## Output example

```
The first element is Some(1)
```

The code above does the following:

1. Create a vector `v` with elements `1`, `2`, and `3`.
2. Use the `get` method to borrow the element at index `0` of the vector.
3. Print the result of the `get` method, which is an `Option` type.

## Helpful links

- [Rust Documentation - Vectors](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [Rust Documentation - Option](https://doc.rust-lang.org/std/option/enum.Option.html)

group: rust-borrow