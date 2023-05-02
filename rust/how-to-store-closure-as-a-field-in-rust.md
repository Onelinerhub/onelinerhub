# How to store closure as a field in Rust
// plain

In Rust, closures can be stored as fields in a struct by using the `Fn` trait. The `Fn` trait is a trait that allows a closure to be called like a function. To store a closure as a field, the closure must be annotated with the `Fn` trait. For example:
```rust
struct MyStruct {
    closure: Box<Fn() -> i32>
}
```
This code creates a struct called `MyStruct` with a field called `closure` that stores a closure that takes no arguments and returns an `i32`.

The closure can then be called like a function by using the `()` operator. For example:
```rust
let my_struct = MyStruct {
    closure: Box::new(|| {
        println!("Hello, world!");
        42
    })
};

let result = my_struct.closure();
println!("Result: {}", result);
```
This code creates an instance of `MyStruct` with a closure that prints "Hello, world!" and returns the value `42`. The closure is then called and the result is printed.

The `Fn` trait is a powerful tool for storing closures as fields in Rust. It allows closures to be called like functions and makes it easy to store and use closures in structs.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Fn Trait](https://doc.rust-lang.org/std/ops/trait.Fn.html)
- [Rust Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)