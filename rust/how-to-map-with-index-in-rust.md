# How to map with index in Rust
// plain

Mapping with index in Rust can be done using the `enumerate()` method on an iterator. This method returns a tuple of the index and the value of the element.

## Example code

```rust
let v = vec![1, 2, 3];

for (i, x) in v.iter().enumerate() {
    println!("Index: {}, Value: {}", i, x);
}
```

## Output example

```
Index: 0, Value: 1
Index: 1, Value: 2
Index: 2, Value: 3
```

## Code explanation

- `let v = vec![1, 2, 3];`: creates a vector `v` with elements `1`, `2`, and `3`.
- `for (i, x) in v.iter().enumerate()`: iterates over the vector `v` and assigns the index `i` and the value `x` of the element to the tuple `(i, x)`.
- `println!("Index: {}, Value: {}", i, x);`: prints the index `i` and the value `x` of the element.

## Helpful links
- [Rust Documentation - Iterator Enumerate](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.enumerate)

group: rust-map