# How to convert a Rust slice to a fixed array?
// plain

To convert a Rust slice to a fixed array, you can use the `std::mem::transmute` function. This function takes a slice and converts it to a fixed array of the same size.

## Example code

```rust
let slice = [1, 2, 3];
let array: [i32; 3] = unsafe { std::mem::transmute(slice) };
```

## Output example

```
[1, 2, 3]
```

## Code explanation

- `let slice = [1, 2, 3];`: This line declares a slice of type `[i32]` with three elements.
- `let array: [i32; 3]`: This line declares a fixed array of type `[i32; 3]` with three elements.
- `unsafe { std::mem::transmute(slice) }`: This line uses the `std::mem::transmute` function to convert the slice to a fixed array.

## Helpful links
- [std::mem::transmute](https://doc.rust-lang.org/std/mem/fn.transmute.html)

group: rust-slice