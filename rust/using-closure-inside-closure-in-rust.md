# Using closure inside closure in Rust
// plain

Closures in Rust allow for the creation of functions that can capture variables from the scope in which they are defined. Closures can also be nested, meaning that one closure can be defined inside another closure. This allows for the creation of more complex functions that can access variables from multiple scopes. For example:
```rust
fn main() {
    let x = 5;
    let closure1 = |y| {
        let closure2 = |z| {
            x + y + z
        };
        closure2
    };
    let result = closure1(3)(4);
    println!("{}", result);
}
```
This code defines a closure, `closure1`, which takes an argument `y` and returns another closure, `closure2`, which takes an argument `z`. `closure2` then returns the sum of `x`, `y`, and `z`. The result of `closure1` is then called with the arguments `3` and `4`, resulting in the output `12`.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Closures Tutorial](https://rust-lang-nursery.github.io/rust-cookbook/fn/closures.html)
- [Rust Closures Explained](https://www.joshmcguigan.com/blog/rust-closures/)

group: rust-closure