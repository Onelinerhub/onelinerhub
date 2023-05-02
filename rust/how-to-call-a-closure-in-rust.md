# How to call a closure in RUst
// plain

In Rust, a closure can be called by using the call operator, which is written as `()`. The closure must be assigned to a variable before it can be called. For example, the following code creates a closure and assigns it to the variable `my_closure`, and then calls it:
```rust
let my_closure = || println!("Hello, world!");
my_closure();
```
The output of this code will be:
```
Hello, world!
```
The call operator `()` is used to call the closure, which will execute the code inside the closure. In this example, the closure prints out the string "Hello, world!".

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Closure Syntax](https://doc.rust-lang.org/rust-by-example/fn/closures.html)
- [Rust Closure Examples](https://www.tutorialspoint.com/rust/rust_closures.htm)