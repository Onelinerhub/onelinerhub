# How do I identify unused variables in Rust?
// plain

Unused variables in Rust can be identified by the compiler. The compiler will throw a warning when it detects an unused variable.

## Example code

```
fn main() {
    let x = 5;
    println!("x is {}", x);
}
```

## Output example

```
warning: unused variable: `x`
  --> src/main.rs:2:9
   |
2  |     let x = 5;
   |         ^ help: if this is intentional, prefix it with an underscore: `_x`
   |
   = note: #[warn(unused_variables)] on by default
```

The compiler will throw a warning when it detects an unused variable. In the example code, the variable `x` is unused and the compiler throws a warning. To prevent the warning, the variable can be prefixed with an underscore, like `_x`.

## Helpful links

- [Rust Documentation - Unused Variables](https://doc.rust-lang.org/book/ch12-03-improving-error-messages.html#unused-variables)

group: rust-variables