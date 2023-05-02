# How to clone closure in Rust
// plain

Cloning a closure in Rust is done by using the `Clone` trait. This trait is implemented for all closures that have the same input and output types. To clone a closure, simply call the `clone` method on the closure. For example, to clone a closure that takes an `i32` and returns an `i32`:
```rust
let my_closure = |x: i32| -> i32 { x + 1 };
let cloned_closure = my_closure.clone();
```
The cloned closure can then be used just like the original closure. For example:
```rust
let result = cloned_closure(5); // result is 6
```
The `Clone` trait is also implemented for closures that take multiple arguments and return multiple values. To clone such a closure, simply call the `clone` method on the closure. For example, to clone a closure that takes two `i32`s and returns an `i32` and a `String`:
```rust
let my_closure = |x: i32, y: i32| -> (i32, String) { (x + y, format!("{} + {}", x, y)) };
let cloned_closure = my_closure.clone();
```
The cloned closure can then be used just like the original closure. For example:
```rust
let result = cloned_closure(5, 10); // result is (15, "5 + 10")
```

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Clone Trait](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [Cloning Closures](https://rustbyexample.com/fn/closures/cloning.html)

group: rust-closure