# Bitwise negation (NOT) usage in Rust
// plain

Bitwise negation (NOT) is a unary operator in Rust that performs a bitwise inversion of its operand. It is represented by the `!` symbol.

For example, the following code block will invert the bits of the number `5`:
```
let x = 5;
let y = !x;
println!("{}", y);
```
The output of this code will be `-6`.

## Code explanation

- `let x = 5;`: This line declares a variable `x` and assigns it the value `5`.
- `let y = !x;`: This line declares a variable `y` and assigns it the value of the bitwise negation of `x`.
- `println!("{}", y);`: This line prints the value of `y` to the console.

## Helpful links
- [Rust Bitwise Operators](https://doc.rust-lang.org/book/ch03-02-operators.html#bitwise-operators)
- [Rust Bitwise Negation (NOT) Operator](https://www.tutorialspoint.com/rust/rust_bitwise_negation_not_operator.htm)

group: rust-bitwise