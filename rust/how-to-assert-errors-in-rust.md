# How to assert errors in Rust
// plain

Rust provides the `assert!` macro to assert errors. This macro takes a boolean expression as an argument and will panic if the expression evaluates to false.

## Code example:

```
let x = 5;
assert!(x == 5);
```

### Output

No output, as the expression evaluates to true.

## Explanation:

1. `let x = 5;`: This statement declares a variable `x` and assigns it the value `5`.
2. `assert!(x == 5);`: This statement uses the `assert!` macro to check if the expression `x == 5` evaluates to true. If it does, the macro does nothing, otherwise it will panic.

## Helpful links:

1. [Rust Documentation - assert!](https://doc.rust-lang.org/std/macro.assert.html)
2. [Rust by Example - assert!](https://doc.rust-lang.org/rust-by-example/macros/assert.html)