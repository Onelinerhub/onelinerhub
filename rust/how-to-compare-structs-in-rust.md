# How to compare structs in Rust
// plain

Comparing structs in Rust is done using the `PartialEq` and `Eq` traits. The `PartialEq` trait allows for comparison of two structs using the `==` operator, while the `Eq` trait allows for comparison of two structs using the `==` and `!=` operators.

## Example code

```rust
use std::cmp::PartialEq;

#[derive(PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = Point { x: 1, y: 2 };
    assert!(p1 == p2);
}
```

## Output example

```
assertion successful
```

## Code explanation


- `use std::cmp::PartialEq`: This imports the `PartialEq` trait from the `std::cmp` module.
- `#[derive(PartialEq)]`: This derives the `PartialEq` trait for the `Point` struct, allowing it to be compared using the `==` operator.
- `let p1 = Point { x: 1, y: 2 };`: This creates a `Point` struct with `x` and `y` values of `1` and `2` respectively.
- `let p2 = Point { x: 1, y: 2 };`: This creates a second `Point` struct with `x` and `y` values of `1` and `2` respectively.
- `assert!(p1 == p2);`: This uses the `==` operator to compare the two `Point` structs, and asserts that they are equal.

## Helpful links

- [Rust Documentation - PartialEq](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)
- [Rust Documentation - Eq](https://doc.rust-lang.org/std/cmp/trait.Eq.html)

group: rust-struct