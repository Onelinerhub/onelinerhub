# How to create an array in Rust lang?
// plain

An array in Rust is a data structure that stores a fixed-size collection of elements of the same type. Arrays are created using square brackets and the elements are separated by commas.

Below is an example of how to create an array in Rust:

```rust
// Create an array of i32 type with 3 elements
let array_example: [i32; 3] = [1, 2, 3];

// Print the array
println!("{:?}", array_example);
```

The output of the above code will be:

```
[1, 2, 3]
```