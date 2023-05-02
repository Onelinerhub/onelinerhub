# How to convert pointer to reference in Rust
// plain

In Rust, you can convert a pointer to a reference by using the `&` operator. For example, if you have a pointer `p` to a type `T`, you can convert it to a reference by using `&p`. This will create a reference to the same value that the pointer points to. The output of this operation will be a reference of type `&T`.
```rust
let p: *const i32 = &10;
let r: &i32 = &p;
```
### Output example
This code will not produce any output.

### Explanation
The `&` operator is used to convert a pointer to a reference. In this example, the pointer `p` is of type `*const i32`, which is a pointer to a constant integer. The `&` operator is used to convert this pointer to a reference of type `&i32`, which is a reference to an integer.

### Relevant links
- [Rust Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust References](https://doc.rust-lang.org/book/ch15-01-box.html)
- [Rust Operators](https://doc.rust-lang.org/book/ch03-02-operators-and-overloading.html)

group: rust-pointers