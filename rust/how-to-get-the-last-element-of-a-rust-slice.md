# How to get the last element of a Rust slice?
// plain

The last element of a Rust slice can be accessed using the `.last()` method. This method returns an `Option<&T>` where `T` is the type of the elements in the slice.

## Example code

```rust
let v = [1, 2, 3];
let last = v.last();
```

## Output example

```
Some(&3)
```

## Code explanation

- `let v = [1, 2, 3];`: This line creates a slice `v` with three elements.
- `let last = v.last();`: This line calls the `.last()` method on the slice `v` and stores the result in the variable `last`.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/std/primitive.slice.html)

group: rust-slice