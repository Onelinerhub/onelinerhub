# Rust map function example
// plain

The `map` function in Rust is a powerful tool for transforming collections of data. It takes a closure as an argument and applies it to each element in the collection, returning a new collection with the transformed elements.

## Example

```rust
let numbers = vec![1, 2, 3];
let doubled_numbers = numbers.map(|x| x * 2);
```

## Output example

```
[2, 4, 6]
```

## Code explanation

- `let numbers = vec![1, 2, 3];`: This line creates a vector of numbers.
- `let doubled_numbers = numbers.map(|x| x * 2);`: This line uses the `map` function to apply the closure `|x| x * 2` to each element in the vector `numbers`, returning a new vector with the transformed elements.

## Helpful links
- [Rust Documentation - Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map)

group: rust-map