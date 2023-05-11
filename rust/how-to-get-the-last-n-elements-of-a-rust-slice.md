# How to get the last n elements of a Rust slice?
// plain

To get the last n elements of a Rust slice, you can use the `.split_last()` method. This method takes a slice and returns a tuple of two slices, the first being the elements before the last n elements, and the second being the last n elements.

```rust
let v = [1, 2, 3, 4, 5];
let (first, last) = v.split_last().unwrap();

println!("First: {:?}, Last: {:?}", first, last);
```

## Output example

```
First: [1, 2, 3], Last: [4, 5]
```

## Code explanation

- `let v = [1, 2, 3, 4, 5];`: This line creates a slice `v` with 5 elements.
- `let (first, last) = v.split_last().unwrap();`: This line uses the `.split_last()` method to split the slice `v` into two slices, `first` and `last`. The `.unwrap()` method is used to unwrap the `Option` returned by `.split_last()`.
- `println!("First: {:?}, Last: {:?}", first, last);`: This line prints the two slices `first` and `last`.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - Option](https://doc.rust-lang.org/std/option/enum.Option.html)

group: rust-slice