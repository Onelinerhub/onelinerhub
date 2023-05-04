# How to map a vector in Rust
// plain

Mapping a vector in Rust is a simple process. It involves using the `map()` method on a vector to apply a function to each element of the vector.

```rust
let v = vec![1, 2, 3];
let v2 = v.map(|x| x * 2);
```

The output of the above code will be `[2, 4, 6]`.

## Code explanation


- `let v = vec![1, 2, 3];`: This creates a vector with the elements `1`, `2`, and `3`.
- `let v2 = v.map(|x| x * 2);`: This uses the `map()` method to apply the function `|x| x * 2` to each element of the vector `v`.
- `[2, 4, 6]`: This is the output of the code, a vector with the elements `2`, `4`, and `6`.

## Helpful links

- [Rust Documentation - Vectors](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [Rust Documentation - Iterators](https://doc.rust-lang.org/std/iter/index.html)

group: rust-map