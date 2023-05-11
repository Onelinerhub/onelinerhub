# How to create a slice from a range in Rust?
// plain

A slice is a reference to a contiguous sequence of elements in a collection. In Rust, you can create a slice from a range using the `std::ops::Range` struct.

## Example code

```rust
let range = 0..10;
let slice = &range[..];
```

## Output example

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Code explanation

- `let range = 0..10;`: This creates a `Range` struct with the start value of 0 and the end value of 10.
- `let slice = &range[..];`: This creates a slice from the `Range` struct. The `..` syntax is used to indicate that the slice should include all elements from the start to the end of the range.

## Helpful links
- [std::ops::Range](https://doc.rust-lang.org/std/ops/struct.Range.html)

group: rust-slice