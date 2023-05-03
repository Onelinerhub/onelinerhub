# How to create boxed array in Rust
// plain

Creating a boxed array in Rust is a simple process. To do so, you must first create a `Box` object, which is a type of pointer that points to a value on the heap. Then, you can use the `into_boxed_slice` method to convert a regular array into a boxed array.

Example code:
```rust
let array = [1, 2, 3];
let boxed_array: Box<[i32]> = array.into_boxed_slice();
```

Output:
```
[1, 2, 3]
```

Code parts with detailed explanation:
- `let array = [1, 2, 3];`: This line creates a regular array with three elements.
- `let boxed_array: Box<[i32]> = array.into_boxed_slice();`: This line creates a `Box` object and assigns it to the variable `boxed_array`. The `into_boxed_slice` method is used to convert the regular array into a boxed array.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - IntoBoxedSlice](https://doc.rust-lang.org/std/primitive.slice.html#method.into_boxed_slice)

group: rust-box