# An example of error in Rust
// plain

An example of an error in Rust is a type mismatch error. This occurs when a variable is assigned a value of a different type than what it was declared as.

For example, the following code will result in a type mismatch error:

```
let x = 5;
x = "Hello";
```

### Output

error[E0308]: mismatched types
 --> src/main.rs:2:5
  |
2 |     x = "Hello";
  |     ^^^^^^^^^^ expected integer, found `&str`

Explanation:
- The variable `x` was declared as an integer on line 1
- On line 2, the variable `x` is being assigned a string value of "Hello"
- This results in a type mismatch error, as the variable `x` was declared as an integer, but is being assigned a string value

## Helpful links:
- [Rust Type Mismatch Error](https://doc.rust-lang.org/error-index.html#E0308)
- [Rust Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)