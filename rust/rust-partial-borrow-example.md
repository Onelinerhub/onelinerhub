# Rust partial borrow example
// plain

Rust allows partial borrows of data structures, which allows you to borrow a part of a data structure without borrowing the entire structure. This can be useful when you want to access a part of a data structure without taking ownership of the entire structure.

## Example code

```rust
let mut data = vec![1, 2, 3];
let first = &data[0];
let second = &data[1];
```

## Output example

```
first = &1
second = &2
```

## Code explanation

- `let mut data = vec![1, 2, 3];`: This line creates a mutable vector containing the elements 1, 2, and 3.
- `let first = &data[0];`: This line creates a reference to the first element of the vector, which is 1.
- `let second = &data[1];`: This line creates a reference to the second element of the vector, which is 2.

## Helpful links
- [Rust Partial Borrows](https://doc.rust-lang.org/book/ch15-02-partial-borrows.html)

group: rust-borrow