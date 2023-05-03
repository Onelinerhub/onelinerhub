# How to check if box is null in Rust
// plain

To check if a box is null in Rust, you can use the `is_null()` method. This method returns `true` if the box is null, and `false` otherwise.

Example code:
```rust
let my_box: Box<i32> = Box::new(5);
let is_null = my_box.is_null();
println!("Is my_box null? {}", is_null);
```

Output:
```
Is my_box null? false
```

Code parts:
- `let my_box: Box<i32> = Box::new(5);`: This line creates a box containing an `i32` value with the value `5`.
- `let is_null = my_box.is_null();`: This line calls the `is_null()` method on the `my_box` box, and stores the result in the `is_null` variable.
- `println!("Is my_box null? {}", is_null);`: This line prints out the result of the `is_null()` method.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box