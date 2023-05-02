# Nested closure example in Rust
// plain

A nested closure example in Rust is a closure that is defined within another closure. This allows for the inner closure to access variables from the outer closure. An example of a nested closure in Rust is shown below:
```rust
fn main() {
    let outer_var = 5;
    let closure = || {
        let inner_var = 10;
        println!("Outer var: {} Inner var: {}", outer_var, inner_var);
    };
    closure();
}
```
### Output example
Outer var: 5 Inner var: 10
### Explanation
The code above defines a variable `outer_var` with the value of 5 and a closure `closure` that prints out the value of `outer_var` and `inner_var`. The `inner_var` is defined within the closure and is not accessible outside of it.
### Relevant links
[Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)

[Nested Closures in Rust](https://doc.rust-lang.org/book/ch13-02-closures-as-input-parameters.html#nested-closures)

[Rust Closure Syntax](https://doc.rust-lang.org/book/ch13-01-closures.html#syntax-for-closures)