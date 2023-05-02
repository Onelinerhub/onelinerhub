# How to drop a closure in Rust
// plain

Dropping a closure in Rust is done by calling the `drop` function on the closure. This will deallocate any resources associated with the closure. For example, the following code creates a closure and then drops it:
```rust
let mut closure = || println!("Hello, world!");
drop(closure);
```
The `drop` function takes a mutable reference to the closure, so it can be used to deallocate any resources associated with the closure. After the `drop` function is called, the closure is no longer valid and cannot be used.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Drop Function](https://doc.rust-lang.org/std/ops/fn.drop.html)
- [Rust Ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)