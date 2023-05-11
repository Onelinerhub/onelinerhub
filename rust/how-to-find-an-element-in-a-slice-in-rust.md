# How to find an element in a slice in Rust?
// plain

Finding an element in a slice in Rust can be done using the `contains()` method. This method takes a reference to the element to be found and returns a boolean value indicating whether the element is present in the slice or not.

## Example code

```rust
let numbers = [1, 2, 3, 4, 5];
let result = numbers.contains(&3);
```

## Output example

```
true
```

## Code explanation

- `let numbers = [1, 2, 3, 4, 5];`: This line creates a slice of numbers.
- `let result = numbers.contains(&3);`: This line calls the `contains()` method on the `numbers` slice, passing a reference to the element to be found (in this case, `3`).
- `true`: This is the output of the example code, indicating that the element `3` is present in the `numbers` slice.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - contains()](https://doc.rust-lang.org/std/primitive.slice.html#method.contains)

group: rust-slice