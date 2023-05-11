# How to create a slice from a pointer in Rust?
// plain

A slice is a data structure that allows access to a contiguous sequence of elements in a collection. In Rust, slices can be created from a pointer using the `std::slice::from_raw_parts` function.

```rust
let ptr = &[1, 2, 3, 4, 5] as *const i32;
let slice = unsafe { std::slice::from_raw_parts(ptr, 5) };
println!("{:?}", slice);
```

## Output example

```
[1, 2, 3, 4, 5]
```

The `std::slice::from_raw_parts` function takes two parameters:

1. `data`: A pointer to the start of the slice.
2. `len`: The length of the slice.

The function returns a `&[T]` slice, where `T` is the type of the elements in the slice.

## Helpful links

- [std::slice::from_raw_parts](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html)

group: rust-slice