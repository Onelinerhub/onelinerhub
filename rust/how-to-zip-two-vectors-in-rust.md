# How to zip two vectors in Rust?
// plain

Zipping two vectors in Rust can be done using the `zip` method. This method takes two iterators and returns a new iterator of tuples, where the first element of each tuple is taken from the first iterator, and the second element is taken from the second iterator.

## Example code

```rust
let v1 = vec![1, 2, 3];
let v2 = vec![4, 5, 6];

let zipped: Vec<_> = v1.iter().zip(v2.iter()).collect();

println!("{:?}", zipped);
```

## Output example

```
[(1, 4), (2, 5), (3, 6)]
```

## Code explanation

- `let v1 = vec![1, 2, 3];`: creates a vector `v1` with elements `1`, `2`, and `3`.
- `let v2 = vec![4, 5, 6];`: creates a vector `v2` with elements `4`, `5`, and `6`.
- `let zipped: Vec<_> = v1.iter().zip(v2.iter()).collect();`: creates a new vector `zipped` by zipping `v1` and `v2` using the `zip` method. The `zip` method takes two iterators and returns a new iterator of tuples, where the first element of each tuple is taken from the first iterator, and the second element is taken from the second iterator. The `collect` method is then used to collect the iterator into a vector.
- `println!("{:?}", zipped);`: prints the vector `zipped` to the console.

## Helpful links
- [Rust Documentation - Iterator::zip](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.zip)
- [Rust Documentation - Iterator::collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-zip