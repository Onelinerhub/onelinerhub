# How to iterate in pairs in Rust
// plain

Iterating in pairs in Rust can be done using the `.zip()` method. This method takes two iterators and returns a new iterator of pairs. The following example code will print out the pairs of numbers from two separate vectors:

```rust
let v1 = vec![1, 2, 3];
let v2 = vec![4, 5, 6];

for (a, b) in v1.iter().zip(v2.iter()) {
    println!("{} {}", a, b);
}
```

## Output example

```
1 4
2 5
3 6
```

## Code explanation

- `let v1 = vec![1, 2, 3];`: creates a vector `v1` with the elements `1, 2, 3`
- `let v2 = vec![4, 5, 6];`: creates a vector `v2` with the elements `4, 5, 6`
- `for (a, b) in v1.iter().zip(v2.iter())`: creates a loop that iterates over the pairs of elements from `v1` and `v2`
- `println!("{} {}", a, b);`: prints out the elements of each pair

## Helpful links
- [Rust Documentation - Iterator::zip](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.zip)

group: rust-loops