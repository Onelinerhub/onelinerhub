# How to borrow as mutable in Rust
// plain

Mutable borrowing in Rust is done using the `&mut` reference type. This type of reference allows you to modify the data that it points to.

Example:
```
let mut x = 5;
let y = &mut x;

*y += 1;

println!("x = {}", x);
```
## Output example

```
x = 6
```

The code above creates a mutable reference `y` to the variable `x`. The `*` operator is used to dereference the reference `y` and modify the value of `x`.

## Code explanation

- `let mut x = 5;`: creates a mutable variable `x` with the value `5`
- `let y = &mut x;`: creates a mutable reference `y` to the variable `x`
- `*y += 1;`: dereferences the reference `y` and modifies the value of `x`
- `println!("x = {}", x);`: prints the value of `x`

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Book](https://doc.rust-lang.org/book/index.html)

group: rust-borrow