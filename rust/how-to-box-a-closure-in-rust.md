# How to box a closure in Rust
// plain

Boxing a closure in Rust is a way to store a closure in a data structure. This allows the closure to be passed around and used in different contexts.

Example code:
```rust
let my_closure = || println!("Hello World!");
let boxed_closure = Box::new(my_closure);
```

Output:
```
Hello World!
```

Code parts:
- `let my_closure = || println!("Hello World!");`: This line creates a closure that prints "Hello World!"
- `let boxed_closure = Box::new(my_closure);`: This line creates a `Box` that stores the closure `my_closure`

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box