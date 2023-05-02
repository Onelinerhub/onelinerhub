# How to declare a closure in Rust
// plain

A closure in Rust is declared using the `|parameters| expression` syntax. The parameters are the values that are passed into the closure, and the expression is the code that is executed when the closure is called. For example, the following code declares a closure that takes two parameters and returns the sum of them:
```rust
let add_two_numbers = |x: i32, y: i32| x + y;
```
The closure can then be called by passing in the appropriate parameters:
```rust
let result = add_two_numbers(2, 3);
```
The result of this call will be `5`. Closures can also be used to capture variables from the surrounding scope, allowing them to be used within the closure. For example:
```rust
let x = 5;
let add_x = |y: i32| x + y;
```
In this example, the closure `add_x` will always add `x` to its parameter, regardless of what `x` is set to in the surrounding scope.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Closure Examples](https://doc.rust-lang.org/rust-by-example/fn/closures.html)
- [Closure Capturing](https://doc.rust-lang.org/book/ch13-02-closures.html#capturing-the-environment-with-closures)