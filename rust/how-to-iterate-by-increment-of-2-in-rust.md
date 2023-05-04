# How to iterate by increment of 2 in Rust
// plain

Iterating by increment of 2 in Rust can be done using the `step_by` method of the `Iterator` trait. This method takes a `usize` argument which is the number of steps to take.

## Example code

```rust
let mut iter = 0..10;
for i in iter.step_by(2) {
    println!("{}", i);
}
```

## Output example

```
0
2
4
6
8
```

## Code explanation

- `let mut iter = 0..10;`: creates an iterator from 0 to 10 (not including 10)
- `for i in iter.step_by(2)`: iterates over the iterator, taking steps of size 2
- `println!("{}", i);`: prints the current value of the iterator

## Helpful links
- [Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.step_by)

group: rust-loops