# How to use closure as an argument in Rust
// plain

Closures can be used as arguments in Rust by using the Fn, FnMut, and FnOnce traits. These traits allow a closure to be passed as an argument to a function. To use a closure as an argument, the closure must be wrapped in one of the traits. For example, the following code shows how to use a closure as an argument to a function:
```
fn call_closure<F: Fn()>(closure: F) {
    closure();
}

fn main() {
    let closure = || println!("Closure called");
    call_closure(closure);
}
```
### Output example
```
Closure called
```
### Explanation
The `call_closure` function takes a generic type `F` which is bounded by the `Fn` trait. This means that any type that implements the `Fn` trait can be passed as an argument to the `call_closure` function. The closure is then called within the function body using the `closure()` syntax.

### Relevant links
[Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
[Fn Trait](https://doc.rust-lang.org/std/ops/trait.Fn.html)
[FnMut Trait](https://doc.rust-lang.org/std/ops/trait.FnMut.html)

group: rust-closure
