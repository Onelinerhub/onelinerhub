# Using closure as an argument in Rust
// plain

Closures in Rust are functions that can capture variables from the scope in which they are defined. Closures can be used as arguments to other functions, allowing for more flexible and powerful code. For example, the following code creates a closure that takes an integer argument and adds it to a variable from the outer scope:
```rust
let x = 5;
let add_x = |y| x + y;
```
The closure `add_x` can then be used as an argument to another function, such as `println!`:
```rust
println!("{}", add_x(10)); // Prints 15
```
The closure captures the value of `x` from the outer scope and adds it to the argument `y` passed to the closure. This allows for more powerful and flexible code, as the same closure can be used in multiple contexts with different values of `x`.

## Helpful links
- [Closures in Rust](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Closures as Arguments](https://doc.rust-lang.org/book/ch13-02-closures-as-arguments.html)
- [Closures in Rust Cheatsheet](https://danielkeep.github.io/tlborm/book/ch13-01-closures.html)