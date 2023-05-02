# How to define closure as variable in Rust
// plain

A closure in Rust is a function that can capture variables from its environment. It can be defined as a variable using the `let` keyword, followed by a name for the closure, and then the closure itself, enclosed in curly braces. For example:
```rust
let my_closure = |x| x + 1;
```
This closure takes an argument `x` and returns `x + 1`. The output of this closure when called with an argument of `2` would be `3`:
```rust
let result = my_closure(2);
println!("{}", result);
```
Output example:
```
3
```
The `|x|` syntax is used to define the parameters of the closure, and the code after the `|` is the body of the closure. The closure can then be used like any other function, with the parameters passed in as arguments.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Closure Syntax](https://doc.rust-lang.org/rust-by-example/fn/closures.html)
- [Rust Closure Capturing](https://doc.rust-lang.org/book/ch13-02-closure-capturing.html)