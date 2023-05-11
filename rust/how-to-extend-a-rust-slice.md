# How to extend a Rust slice?
// plain

A Rust slice can be extended using the `extend()` method. This method takes an iterator as an argument and appends each element of the iterator to the slice.

```rust
let mut v = vec![1, 2, 3];
let mut s = &mut v[..];
s.extend([4, 5].iter());

println!("{:?}", s);
```

## Output example

```
[1, 2, 3, 4, 5]
```

The code above creates a vector `v` with elements `1`, `2`, and `3`. A mutable slice `s` is created from the vector. The `extend()` method is then used to append the elements `4` and `5` to the slice. The output of the code is `[1, 2, 3, 4, 5]`.

Parts of the code:
- `let mut v = vec![1, 2, 3];`: creates a vector `v` with elements `1`, `2`, and `3`.
- `let mut s = &mut v[..];`: creates a mutable slice `s` from the vector `v`.
- `s.extend([4, 5].iter());`: uses the `extend()` method to append the elements `4` and `5` to the slice `s`.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
- [Rust Documentation - Iterator](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)

group: rust-slice