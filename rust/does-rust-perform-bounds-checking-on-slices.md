# Does Rust perform bounds checking on slices?
// plain

Yes, Rust performs bounds checking on slices. This is done to ensure that the slice does not exceed the length of the underlying array.

For example, the following code will cause a panic due to an out-of-bounds access:

```
let arr = [1, 2, 3];
let slice = &arr[..4];
```

## Output example


```
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 4', src/libcore/slice/mod.rs:2706:10
```

The code above attempts to create a slice of `arr` from index 0 to index 4, which is out of bounds since `arr` only has 3 elements.

## Helpful links

- [Rust Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [Rust Bounds Checking](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#bounds-checking)

group: rust-slice