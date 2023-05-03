# How to change box value in Rust
// plain

Changing the value of a box in Rust is done using the `*` operator. This operator dereferences the box, allowing you to access the value stored inside.

```rust
let mut x = Box::new(5);
*x = 10;
println!("{}", x);
```

Output:
```
10
```

The code above creates a box with the value `5` and then dereferences it using the `*` operator. This allows us to change the value stored inside the box to `10`. Finally, we print out the new value of the box.

Code parts:

1. `let mut x = Box::new(5);` - creates a box with the value `5`
2. `*x = 10;` - dereferences the box and assigns the value `10` to it
3. `println!("{}", x);` - prints out the new value of the box

## Helpful links

- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - Dereferencing](https://doc.rust-lang.org/book/ch15-02-deref.html)

group: rust-box