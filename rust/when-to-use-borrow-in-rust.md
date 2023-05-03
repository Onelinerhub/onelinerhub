# When to use borrow in Rust
// plain

Borrowing in Rust is a way to temporarily take ownership of a value without taking ownership of it permanently. It is used when you want to use a value without taking ownership of it, such as when passing a value to a function.

Example:
```
let mut x = 5;
let y = &x;

println!("x = {}", x);
println!("y = {}", y);
```

## Output example

```
x = 5
y = 5
```

In this example, `x` is a mutable variable with the value of 5. `y` is a reference to `x`, which means that `y` borrows the value of `x` without taking ownership of it. `y` can be used to access the value of `x`, but `x` still owns the value and can be modified.

The main benefit of borrowing is that it allows you to use a value without taking ownership of it, which can be useful in many situations. For example, when passing a value to a function, you can borrow the value instead of taking ownership of it.

List of ## Code explanation


1. `let mut x = 5;` - This line declares a mutable variable `x` with the value of 5.
2. `let y = &x;` - This line declares a reference to `x`, which means that `y` borrows the value of `x` without taking ownership of it.
3. `println!("x = {}", x);` - This line prints the value of `x` to the console.
4. `println!("y = {}", y);` - This line prints the value of `y` to the console.

## Helpful links

- [Rust Documentation - Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rust by Example - Borrowing](https://doc.rust-lang.org/rust-by-example/scope/borrow.html)

group: rust-borrow