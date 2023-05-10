# How to zip vectors of different lengths in Rust?
// plain

Zipping vectors of different lengths in Rust can be done using the `zip` method from the `Iterator` trait. This method takes two iterators and returns a new iterator of pairs, where the first element of each pair is taken from the first iterator, and the second element is taken from the second iterator.

## Example code

```rust
let v1 = vec![1, 2, 3];
let v2 = vec![4, 5];

let zipped: Vec<_> = v1.iter().zip(v2.iter()).collect();

println!("{:?}", zipped);
```

## Output example

```
[(1, 4), (2, 5)]
```

## Code explanation

- `let v1 = vec![1, 2, 3];`: creates a vector `v1` with elements `1`, `2`, and `3`.
- `let v2 = vec![4, 5];`: creates a vector `v2` with elements `4` and `5`.
- `let zipped: Vec<_> = v1.iter().zip(v2.iter()).collect();`: creates a new vector `zipped` by zipping the two vectors `v1` and `v2` using the `zip` method from the `Iterator` trait. The `zip` method takes two iterators and returns a new iterator of pairs, where the first element of each pair is taken from the first iterator, and the second element is taken from the second iterator.
- `println!("{:?}", zipped);`: prints the vector `zipped` to the console.

## Helpful links
- [Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-zip