# How to send box in Rust
// plain

Sending a box in Rust is a simple process. To do so, you must first create a `Box` type with the `Box` keyword.

```rust
let my_box = Box::new(5);
```

This creates a box containing the value `5`. To send the box, you must use the `std::mem::swap` function.

```rust
let mut target = 0;
std::mem::swap(&mut target, &mut my_box);
```

This swaps the contents of `target` and `my_box`, effectively sending the box.

1. Create a `Box` type with the `Box` keyword: `let my_box = Box::new(5);`
2. Use the `std::mem::swap` function to swap the contents of `target` and `my_box`: `std::mem::swap(&mut target, &mut my_box);`

## Helpful links

- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - std::mem::swap](https://doc.rust-lang.org/std/mem/fn.swap.html)

group: rust-box