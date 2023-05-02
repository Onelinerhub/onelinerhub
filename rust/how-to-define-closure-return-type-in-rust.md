# How to define closure return type in RUst
// plain

In Rust, closure return types can be defined by using the `->` operator followed by the return type. For example, the following closure returns a `String`:
```rust
let closure = |x| -> String { format!("The value of x is {}", x) };
```
The return type of the closure can also be inferred by the compiler, so the above example can be written as:
```rust
let closure = |x| { format!("The value of x is {}", x) };
```
The return type of the closure can also be explicitly set to `()` if the closure does not return a value. For example:
```rust
let closure = |x| -> () { println!("The value of x is {}", x) };
```
## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Closure Return Types](https://doc.rust-lang.org/book/ch13-02-closures-as-input-parameters.html#return-types-for-closures)
- [Rust Closure Syntax](https://doc.rust-lang.org/book/ch13-02-closures-as-input-parameters.html#syntax-for-closures)