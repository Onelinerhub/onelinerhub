# Are there named closure in Rust
// plain

No, there are no named closures in Rust. Closures are anonymous functions that capture their environment and can be passed around like any other value. Closures are declared using the `|parameters| expression` syntax. For example, the following closure captures its environment and adds two to its parameter:
```rust
let add_two = |x: i32| x + 2;
```
The output of this closure would be the value of `x` plus two.

Closures are useful for creating functions that can be passed around and used in different contexts. They are also useful for creating functions that can be used to modify the environment they are declared in.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Closure Examples](https://doc.rust-lang.org/book/ch13-02-closures.html)
- [Closure Traits](https://doc.rust-lang.org/std/ops/trait.Fn.html)

group: rust-closure