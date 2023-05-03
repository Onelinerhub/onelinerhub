# How to get box value in Rust
// plain

Getting the value of a box in Rust is done by using the `deref` method. This method returns a reference to the value stored in the box.

Example code:
```rust
let x = Box::new(5);
let y = *x;
println!("{}", y);
```
Output:
```
5
```

The code above creates a box with the value 5 and then uses the `deref` method to get the value stored in the box. The `*` operator is used to dereference the box and get the value. The value is then printed using the `println!` macro.

Code parts:
- `let x = Box::new(5);`: creates a box with the value 5
- `let y = *x;`: uses the `deref` method to get the value stored in the box
- `println!("{}", y);`: prints the value using the `println!` macro

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - Deref](https://doc.rust-lang.org/std/ops/trait.Deref.html)

group: rust-box