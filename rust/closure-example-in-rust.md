# Closure example in Rust
// plain

Closures in Rust are anonymous functions that can capture variables from the scope in which they are defined. They are often used to create functions that can be passed as arguments to other functions. An example of a closure in Rust is shown below:
```rust
let add_one = |x: i32| -> i32 { x + 1 };
```
This closure takes an argument of type `i32` and returns a value of type `i32`. The closure captures no variables from the surrounding scope, so it is a "free" closure.

When called, the closure will add one to the argument passed in:

```rust
let result = add_one(5);
println!("The result is {}", result);
```

### Output example

```
The result is 6
```

### Explanation

The closure `add_one` is defined using the `|x: i32| -> i32 { x + 1 }` syntax. This syntax defines a closure that takes an argument of type `i32` and returns a value of type `i32`. The body of the closure is `x + 1`, which adds one to the argument passed in.

When the closure is called, the argument is passed in and the body of the closure is executed. In this example, the argument `5` is passed in, so the result of the closure is `6`.

### Relevant links

- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Closure Syntax](https://doc.rust-lang.org/book/ch13-02-closure-syntax.html)
- [Rust Closure Capturing](https://doc.rust-lang.org/book/ch13-03-closure-capturing.html)