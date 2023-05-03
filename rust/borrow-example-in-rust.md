# Borrow example in Rust
// plain

A borrow in Rust is when a variable is given temporary access to a resource. This allows the variable to use the resource without taking ownership of it.

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

In this example, `x` is a mutable variable with the value of 5. `y` is a borrow of `x`, meaning it has access to the value of `x` without taking ownership of it. When we print out the values of `x` and `y`, we can see that they are both 5.

## Code explanation

- `let mut x = 5;`: This declares a mutable variable `x` with the value of 5.
- `let y = &x;`: This declares a borrow of `x` called `y`.
- `println!("x = {}", x);`: This prints out the value of `x`.
- `println!("y = {}", y);`: This prints out the value of `y`.

## Helpful links
- [Rust Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-borrow