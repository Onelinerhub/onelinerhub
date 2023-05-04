# How to map an array in Rust
// plain

Mapping an array in Rust is a simple process. It involves using the `map` method on an array to apply a function to each element of the array.

```rust
let arr = [1, 2, 3];
let mapped_arr = arr.map(|x| x * 2);
```

The output of the above code will be `[2, 4, 6]`.

## Code explanation


- `let arr = [1, 2, 3]`: This creates an array with the elements `1`, `2`, and `3`.
- `let mapped_arr = arr.map(|x| x * 2)`: This uses the `map` method to apply the function `x * 2` to each element of the `arr` array.
- `[2, 4, 6]`: This is the output of the code, which is an array with the elements `2`, `4`, and `6`.

## Helpful links

- [Rust Documentation - Iterators](https://doc.rust-lang.org/std/iter/index.html)
- [Rust Documentation - Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-map