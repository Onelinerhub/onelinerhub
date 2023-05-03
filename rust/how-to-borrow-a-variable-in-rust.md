# How to borrow a variable in Rust
// plain

Borrowing a variable in Rust is done using the `&` operator. This operator creates a reference to the variable, allowing it to be used without taking ownership of it.

```rust
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

The code above creates a mutable variable `x` and a reference `y` to it. The `&` operator creates a reference to `x` which can be used to access its value without taking ownership of it.

Parts of the code:
- `let mut x = 5;`: creates a mutable variable `x` with the value `5`
- `let y = &x;`: creates a reference `y` to the variable `x`
- `println!("x = {}", x);`: prints the value of `x`
- `println!("y = {}", y);`: prints the value of `y`, which is the same as the value of `x`

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Book - References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-borrow