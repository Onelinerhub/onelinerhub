# How to borrow option value in Rust
// plain

Rust provides a powerful borrowing system that allows you to borrow values from one place and use them in another. This is done through the `&` operator, which creates a reference to a value. The reference can then be used to access the value without taking ownership of it.

```rust
let x = 5;
let y = &x;

println!("x = {}", x);
println!("y = {}", y);
```

## Output example

```
x = 5
y = 5
```

The code above creates a variable `x` with the value `5`, and then creates a reference to `x` called `y`. The reference `y` can then be used to access the value of `x` without taking ownership of it.

The borrowing system in Rust is very powerful and allows for a variety of different types of borrowing. For example, you can borrow a value mutably, which allows you to modify the value without taking ownership of it.

```rust
let mut x = 5;
let y = &mut x;

*y = 10;

println!("x = {}", x);
println!("y = {}", y);
```

## Output example

```
x = 10
y = 10
```

In this example, the variable `x` is declared as mutable, and then a mutable reference to `x` is created called `y`. The reference `y` can then be used to modify the value of `x` without taking ownership of it.

For more information about Rust's borrowing system, see the [Rust Book](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html).

group: rust-borrow