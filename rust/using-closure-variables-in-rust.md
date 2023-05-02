# Using closure variables in Rust
// plain

Closure variables in Rust allow you to store values in a closure and access them later. Closures are functions that can capture variables from the scope in which they are defined. Closures can be used to create functions that can be passed around and used in different contexts. To use closure variables, you must first define a closure and then use the `move` keyword to capture the variables. You can then access the variables within the closure using the `&` operator. An example of using closure variables is shown below:
```
let mut x = 5;
let closure = move |y| {
    x += y;
};
closure(3);
println!("x = {}", x);
```
This code creates a closure that captures the variable `x` and adds the value of `y` to it. The closure is then called with the value `3` and the value of `x` is printed. The output of this code is `x = 8`.

Using closure variables can be a powerful tool for creating functions that can be used in different contexts. It can also be used to create functions that can be passed around and used in different parts of a program.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Closure Variables](https://doc.rust-lang.org/book/ch13-02-closures-and-capturing.html)
- [Rust by Example - Closures](https://doc.rust-lang.org/rust-by-example/fn/closures.html)