# How to make closure call itself in Rust
// plain

Closures in Rust can be called recursively by using the self keyword. To do this, the closure must be assigned to a variable, and then the variable can be used to call the closure. The following ## Code example shows how to make a closure call itself:
```rust
let mut closure = || {
    println!("Closure called");
    closure();
};
closure();
```
### Output example
```
Closure called
Closure called
Closure called
...
```
### Explanation
The ## Code example above creates a mutable variable `closure` which is assigned to a closure. The closure prints a message and then calls itself using the `closure()` syntax. Finally, the closure is called once to start the recursive loop.

The `||` syntax is used to create a closure, and the `mut` keyword is used to make the closure mutable so that it can be called multiple times.

### Relevant links
- [Closures in Rust](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Recursive Closures in Rust](https://doc.rust-lang.org/book/ch13-02-recursion.html)
- [Mutable Variables in Rust](https://doc.rust-lang.org/book/ch03-02-data-types.html#mutable-variables)