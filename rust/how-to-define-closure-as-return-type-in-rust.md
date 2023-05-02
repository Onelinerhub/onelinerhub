# How to define closure as return type in Rust
// plain

In Rust, a closure can be defined as a return type by using the `Fn` trait. The `Fn` trait is a trait that allows a closure to be called like a function. To define a closure as a return type, the `Fn` trait must be specified in the return type declaration. For example:

```rust
fn my_function() -> impl Fn(i32) -> i32 {
    |x| x + 1
}
```

In this example, the closure `|x| x + 1` is defined as the return type of the function `my_function`. The closure takes an `i32` as an argument and returns an `i32`.

The output of this example would be the closure itself, which can then be used like a function. For example:

```rust
let my_closure = my_function();
let result = my_closure(5);

println!("The result is {}", result);
```

Output example:

```
The result is 6
```

The `Fn` trait is a powerful tool for defining closures as return types in Rust. It allows closures to be used like functions, and can be used to create powerful and expressive code.

## Helpful links

- [The Rust Programming Language - Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [The Rust Programming Language - Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [The Rust Programming Language - Return Values](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#return-values)