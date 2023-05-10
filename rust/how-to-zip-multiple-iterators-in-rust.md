# How to zip multiple iterators in Rust?
// plain

Zipping multiple iterators in Rust can be done using the `zip()` method from the `Iterator` trait. This method takes two or more iterators and returns a new iterator of tuples, where the first element of the tuple is from the first iterator, the second element from the second iterator, and so on.

## Example code

```rust
let a = [1, 2, 3];
let b = [4, 5, 6];

let zipped = a.iter().zip(b.iter());

for t in zipped {
    println!("{:?}", t);
}
```

## Output example

```
(1, 4)
(2, 5)
(3, 6)
```

## Code explanation

- `let a = [1, 2, 3];`: creates an array of integers
- `let b = [4, 5, 6];`: creates another array of integers
- `let zipped = a.iter().zip(b.iter());`: creates a new iterator of tuples by zipping the two iterators
- `for t in zipped {`: iterates over the zipped iterator
- `println!("{:?}", t);`: prints the tuple

## Helpful links
- [Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.zip)

group: rust-zip