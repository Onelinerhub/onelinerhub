# Rust null value example
// plain

Null values in Rust are represented by the `Option` enum. `Option` is an enum with two variants, `Some` and `None`. `Some` is used to wrap a value, while `None` is used to indicate the absence of a value.

## Example code

```rust
let x: Option<i32> = None;
```

This code creates a variable `x` of type `Option<i32>` and assigns it the value `None`. This indicates that `x` does not have a value.

## Helpful links
- [Rust Option Enum](https://doc.rust-lang.org/std/option/enum.Option.html)

group: rust-null