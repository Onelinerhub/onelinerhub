# How to return borrow in Rust
// plain

Returning a borrow in Rust is a process of returning ownership of a borrowed value back to its original owner. This is done by using the `return` keyword.

Example:
```
fn main() {
    let mut x = 5;
    let y = &mut x;
    *y += 1;
    println!("x = {}", x);
    return y;
}
```
## Output example

```
x = 6
```

The code above borrows the value of `x` and stores it in `y`. The value of `x` is then incremented by 1. After that, the ownership of `y` is returned to its original owner, `x`.

## Code explanation

- `let mut x = 5;`: Declares a mutable variable `x` with an initial value of 5.
- `let y = &mut x;`: Borrows the value of `x` and stores it in `y`.
- `*y += 1;`: Increments the value of `y` by 1.
- `return y;`: Returns the ownership of `y` back to its original owner, `x`.

## Helpful links
- [Rust Reference - Return](https://doc.rust-lang.org/reference/expressions/return-expr.html)
- [Rust Reference - Borrowing](https://doc.rust-lang.org/reference/expressions/borrow-expr.html)

group: rust-borrow