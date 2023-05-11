# How to create an empty slice in Rust?
// plain

Creating an empty slice in Rust is easy. You can use the `Vec::new()` method to create an empty slice. The following example code creates an empty slice of type `i32`:

```rust
let empty_slice: Vec<i32> = Vec::new();
```

The output of the above code is an empty slice:

```
[]
```

The code consists of two parts:

1. `let empty_slice: Vec<i32>` - This declares a variable `empty_slice` of type `Vec<i32>`, which is a slice of type `i32`.

2. `Vec::new()` - This creates an empty slice of type `i32`.

For more information, see the [Rust documentation](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.new).

group: rust-slice