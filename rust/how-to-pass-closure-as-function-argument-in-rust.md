# How to pass closure as function argument in Rust
// plain

In Rust, closures can be passed as function arguments by using the `Fn` trait. To do this, the closure must be declared as a parameter of the function, and the `Fn` trait must be specified for the parameter. For example, the following code passes a closure as an argument to a function:
```rust
fn call_closure<F: Fn()>(closure: F) {
    closure();
}

fn main() {
    let closure = || println!("Closure called");
    call_closure(closure);
}
```
The output of this code is:
```
Closure called
```
In this example, the closure is declared as a parameter of the `call_closure` function, and the `Fn` trait is specified for the parameter. This allows the closure to be passed as an argument to the function. Inside the function, the closure is called using the `closure()` syntax.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Fn Trait](https://doc.rust-lang.org/std/ops/trait.Fn.html)
- [Passing Closures as Arguments](https://doc.rust-lang.org/rust-by-example/fn/closures/input_parameters.html)

group: rust-closure