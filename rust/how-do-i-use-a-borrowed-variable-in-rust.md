# How do I use a borrowed variable in Rust?
// plain

Using a borrowed variable in Rust is a way to access a variable without taking ownership of it. This is done by using the `&` operator to create a reference to the variable.

For example:
```
let x = 5;
let y = &x;
```
This creates a reference `y` to the variable `x`.

## Code explanation

- `let x = 5;`: This creates a variable `x` with the value `5`.
- `let y = &x;`: This creates a reference `y` to the variable `x`.

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/expressions/operator-expr.html#references-and-borrowing)
- [Rust Book](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-variables