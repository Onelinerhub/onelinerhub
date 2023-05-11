# How to create a subslice from a Rust slice?
// plain

Creating a subslice from a Rust slice is a simple process. The `&[T]` type provides the `slice` method which takes two indices and returns a subslice of the original slice.

```rust
let v = [1, 2, 3, 4, 5];
let s = &v[1..3];
println!("{:?}", s);
```

## Output example

```
[2, 3]
```

The code above creates a subslice `s` from the original slice `v` by passing two indices `1` and `3` to the `slice` method. The output is a subslice containing elements from index `1` to index `3` (not including index `3`).

Parts of the code:
- `let v = [1, 2, 3, 4, 5];`: creates a slice `v` containing elements `1`, `2`, `3`, `4`, and `5`.
- `let s = &v[1..3];`: creates a subslice `s` from the original slice `v` by passing two indices `1` and `3` to the `slice` method.
- `println!("{:?}", s);`: prints the subslice `s` to the console.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)

group: rust-slice