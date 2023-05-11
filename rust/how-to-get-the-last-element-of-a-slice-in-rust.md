# How to get the last element of a slice in Rust?
// plain

The last element of a slice in Rust can be obtained using the `.last()` method. This method returns an `Option<&T>` where `T` is the type of the elements in the slice.

## Example code

```rust
let v = [1, 2, 3];
let last = v.last();
```

## Output example

```
Some(&3)
```

The `.last()` method returns an `Option<&T>` which is an enum with two variants: `Some(&T)` and `None`. If the slice is empty, `None` is returned, otherwise `Some(&T)` is returned where `T` is the type of the elements in the slice.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - Option](https://doc.rust-lang.org/std/option/enum.Option.html)

group: rust-slice