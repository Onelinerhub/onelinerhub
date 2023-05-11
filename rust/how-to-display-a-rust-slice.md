# How to display a Rust slice?
// plain

A Rust slice is a data structure that allows access to a contiguous sequence of elements in a collection. It is a reference to a contiguous region of memory and can be used to view the underlying data in the collection.

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

## Code explanation

- `let numbers = [1, 2, 3, 4, 5];`: This line creates an array of numbers.
- `let slice = &numbers[1..3];`: This line creates a slice of the array, starting at index 1 and ending at index 3.
- `println!("{:?}", slice);`: This line prints the slice to the console.

## Helpful links
- [Rust Slice Documentation](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Slicing Tutorial](https://doc.rust-lang.org/book/ch04-03-slices.html)

group: rust-slice