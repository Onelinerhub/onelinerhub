# How to push an element to a Rust slice?
// plain

To push an element to a Rust slice, you can use the `push()` method. This method takes a single argument, which is the element to be added to the end of the slice.

```rust
let mut my_slice = vec![1, 2, 3];
my_slice.push(4);
```

The output of the above code will be `[1, 2, 3, 4]`.

The `push()` method has the following parts:

- `let mut my_slice`: This declares a mutable variable `my_slice` of type `Vec<i32>`.
- `vec![1, 2, 3]`: This creates a vector with the elements `1`, `2`, and `3`.
- `my_slice.push(4)`: This adds the element `4` to the end of the vector `my_slice`.

## Helpful links

- [Vec::push()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.push)

group: rust-slice