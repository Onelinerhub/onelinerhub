# How to borrow with lifetime in Rust
// plain

Rust provides a powerful feature called 'lifetimes' which allows you to borrow data from one part of your code and use it in another. This is done by specifying a lifetime for a reference, which is a period of time during which the reference is valid.

```rust
fn main() {
    let x = 5;
    let y = &x;
    println!("x = {}", x);
    println!("y = {}", y);
}
```

## Output example

```
x = 5
y = 5
```

The code above shows how to borrow with lifetime in Rust. The `let x = 5` statement creates a variable `x` with the value `5`. The `let y = &x` statement creates a reference `y` to the variable `x`. The `&` symbol is used to create a reference. The lifetime of the reference `y` is the same as the lifetime of the variable `x`.

List of ## Code explanation

- `let x = 5`: creates a variable `x` with the value `5`
- `let y = &x`: creates a reference `y` to the variable `x`
- `&` symbol: used to create a reference
- `println!("x = {}", x)`: prints the value of `x`
- `println!("y = {}", y)`: prints the value of `y`

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Book](https://doc.rust-lang.org/book/index.html)

group: rust-borrow