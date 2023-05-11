# How to get the end of a slice in Rust?
// plain

The `end` of a slice in Rust can be obtained using the `.end` method. This method returns an `Option<&T>` where `T` is the type of the slice.

## Example code

```rust
let v = [1, 2, 3, 4, 5];
let s = &v[1..4];
let end = s.end();
println!("{:?}", end);
```

## Output example

```
Some(&5)
```

The code above creates a slice `s` from the array `v` and then uses the `.end` method to get the end of the slice. The output is `Some(&5)` which is the last element of the slice.

Parts of the code:
- `let v = [1, 2, 3, 4, 5];`: creates an array `v` with elements `1`, `2`, `3`, `4`, and `5`.
- `let s = &v[1..4];`: creates a slice `s` from the array `v` with elements `2`, `3`, and `4`.
- `let end = s.end();`: uses the `.end` method to get the end of the slice `s`.
- `println!("{:?}", end);`: prints the output of the `.end` method.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
- [Rust Documentation - Option](https://doc.rust-lang.org/stable/std/option/enum.Option.html)

group: rust-slice