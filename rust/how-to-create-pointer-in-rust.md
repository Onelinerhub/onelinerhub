# How to create pointer in Rust
// plain

Creating a pointer in Rust is done by using the `&` operator. This operator creates a reference to a value, which can then be used to access the value. For example, to create a pointer to an integer, you can use the following code:
```rust
let x = 5;
let x_ptr = &x;
```
The `x_ptr` variable now holds a reference to the `x` variable, which can be used to access the value of `x`. To access the value of `x` through the pointer, you can use the `*` operator, like so:
```rust
let x = 5;
let x_ptr = &x;
println!("x = {}", *x_ptr);
```
This will print out `x = 5`.

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Operators](https://doc.rust-lang.org/book/ch04-02-operators-and-overloading.html)

group: rust-pointers