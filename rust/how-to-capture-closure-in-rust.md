# How to capture closure in Rust
// plain

Capturing a closure in Rust is done by using the `Fn` trait. This trait allows a closure to be stored in a variable and then called later. To capture a closure, the variable must be declared with the `Fn` trait and the closure must be passed as an argument. For example:
```rust
let my_closure = |x| x + 1;
let my_fn = Fn::new(my_closure);
```
The `Fn` trait is implemented for all closures that take up to three parameters and return a value. The closure can then be called using the `call` method. For example:
```rust
let result = my_fn.call(2);
```
This will call the closure with the argument `2` and return the result `3`.

Detailed information about the `Fn` trait can be found in the [Rust documentation](https://doc.rust-lang.org/std/ops/trait.Fn.html). Additionally, the [Rust book](https://doc.rust-lang.org/book/ch13-01-closures.html) provides a more in-depth explanation of closures in Rust.