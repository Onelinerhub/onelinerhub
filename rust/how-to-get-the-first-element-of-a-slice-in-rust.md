# How to get the first element of a slice in Rust?
// plain

The first element of a slice in Rust can be obtained using the `get` method. This method takes an index as an argument and returns an `Option` type.

## Example code

```rust
let slice = [1, 2, 3];
let first_element = slice.get(0);
```

## Output example

```
Some(1)
```

The `get` method returns an `Option` type, which is an enum with two variants: `Some` and `None`. If the index is valid, `Some` is returned with the element as its value. If the index is out of bounds, `None` is returned.

## Code explanation

- `let slice = [1, 2, 3];`: creates a slice with three elements
- `let first_element = slice.get(0);`: calls the `get` method on the slice with the index `0` as an argument

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/std/primitive.slice.html)
- [Rust Documentation - Option](https://doc.rust-lang.org/stable/std/option/enum.Option.html)

group: rust-slice