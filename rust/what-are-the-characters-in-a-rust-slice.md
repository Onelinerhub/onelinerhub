# What are the characters in a Rust slice?
// plain

A Rust slice is a data structure that allows access to a contiguous sequence of elements in a collection. It is a reference to a contiguous sequence of elements in a collection, and it is represented by the `&[T]` type.

## Example code

```rust
let numbers = [1, 2, 3, 4, 5];
let slice = &numbers[1..3];
println!("{:?}", slice);
```

## Output example

```
[2, 3]
```

The code above creates a slice of the `numbers` array, starting at index 1 and ending at index 3. The slice contains the elements at indices 1 and 2, which are `2` and `3`.

The `&[T]` type is a reference to a contiguous sequence of elements in a collection. It is a generic type, so it can be used with any type. The elements in the slice must all be of the same type.

## Helpful links

- [Rust Slice Documentation](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Slices Tutorial](https://doc.rust-lang.org/rust-by-example/slice.html)

group: rust-slice