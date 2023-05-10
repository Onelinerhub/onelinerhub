# How to zip arrays in Rust?
// plain

Zipping two arrays in Rust can be done using the `zip` method from the `Iterator` trait. This method takes two iterators and returns a new iterator of tuples, where the first element of each tuple is taken from the first iterator, and the second element is taken from the second iterator.

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

- `let a = [1, 2, 3];`: creates an array `a` with elements `1`, `2`, and `3`.
- `let b = [4, 5, 6];`: creates an array `b` with elements `4`, `5`, and `6`.
- `let zipped = a.iter().zip(b.iter());`: creates a new iterator `zipped` by zipping the iterators of `a` and `b`.
- `for t in zipped {`: iterates over the tuples in `zipped`.
- `println!("{:?}", t);`: prints the tuple `t` in a debug format.

## Helpful links
- [Iterator trait documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-zip