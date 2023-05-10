# What is the default value of a variable in Rust?
// plain

The default value of a variable in Rust is `()`, which is an empty tuple. This is also known as the unit type.

```rust
let x = ();
println!("{:?}", x);
```

## Output example

```
()
```

The code above declares a variable `x` with the default value `()`. The `println!` macro prints the value of `x` which is `()`.

- `let x = ();` declares a variable `x` with the default value `()`.
- `println!("{:?}", x);` prints the value of `x` which is `()`.

## Helpful links
- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [Rust Documentation - Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#the-unit-type-and-the-unit-like-structs)

group: rust-variables