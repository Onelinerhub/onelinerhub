# How do I create an array of strings in Rust?
// plain

Creating an array of strings in Rust is a simple task. To do so, you can use the `vec!` macro. This macro takes a list of values and creates a vector from them. For example, the following code creates an array of strings:

```rust
let array_of_strings = vec!["Hello", "World"];
```

The `vec!` macro creates a `Vec<T>` type, which is a vector of type `T`. In this case, `T` is a `&str`, which is a string slice. The `vec!` macro takes a list of values and creates a vector from them.

The output of the example code is a `Vec<&str>` type, which is a vector of string slices:

```
[Hello, World]
```

For more information, see the [Rust documentation on vectors](https://doc.rust-lang.org/std/vec/struct.Vec.html).