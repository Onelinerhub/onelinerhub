# Const pointer example in Rust
// plain

A const pointer in Rust is a pointer that points to a value that cannot be changed. An example of a const pointer in Rust is shown below:
```rust
let x = 5;
let y = &x;
let z: &const i32 = y;
```
In this example, `x` is an `i32` variable with the value `5`. `y` is a pointer to `x`, and `z` is a const pointer to `y`.

### Output example
No output is produced from this code.

### Explanation
The `let x = 5;` statement creates an `i32` variable `x` with the value `5`. The `let y = &x;` statement creates a pointer `y` to `x`. The `let z: &const i32 = y;` statement creates a const pointer `z` to `y`.

### Relevant links
- [Rust Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Const Pointers](https://doc.rust-lang.org/book/ch19-02-advanced-features.html#const-pointers)
- [Rust Reference](https://doc.rust-lang.org/reference/items/references.html)

group: rust-pointers