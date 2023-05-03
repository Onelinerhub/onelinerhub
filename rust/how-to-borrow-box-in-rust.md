# How to borrow box in Rust
// plain

Borrowing a box in Rust is a way to temporarily take ownership of a value without taking ownership of the value itself. This is done using the `&` operator.

```
let mut x = Box::new(5);
let y = &mut x;
```

The code above creates a `Box` containing the value `5`, and then creates a reference to the `Box` called `y`. This reference can be used to access the value inside the `Box` without taking ownership of the `Box` itself.

The ## Code explanation


- `let mut x = Box::new(5);`: This line creates a `Box` containing the value `5`.
- `let y = &mut x;`: This line creates a reference to the `Box` called `y`.

## Helpful links

- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-borrow