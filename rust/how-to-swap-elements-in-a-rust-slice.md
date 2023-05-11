# How to swap elements in a Rust slice?
// plain

Swapping elements in a Rust slice can be done using the `swap` method. This method takes two indices as arguments and swaps the elements at those indices.

## Example

```
let mut v = [1, 2, 3, 4];
v.swap(0, 3);
```
## Output example

```
[4, 2, 3, 1]
```

## Code explanation

- `let mut v = [1, 2, 3, 4];`: Declares a mutable slice `v` with elements `1`, `2`, `3`, and `4`.
- `v.swap(0, 3);`: Calls the `swap` method on `v` with arguments `0` and `3`, which swaps the elements at indices `0` and `3`.

## Helpful links
- [Rust Documentation - std::slice::SliceIndex](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html)

group: rust-slice