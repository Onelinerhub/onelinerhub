# Bitwise XOR operator usage in Rust
// plain

The bitwise XOR operator (`^`) is a binary operator in Rust that performs a bitwise exclusive OR operation on two operands. It returns a result that has a bit set if either, but not both, of the corresponding bits of the two operands is set.

## Example

```
let a = 0b1010;
let b = 0b1100;

let result = a ^ b;
println!("{:b}", result);
```

## Output example

```
0110
```

## Code explanation

- `let a = 0b1010;`: This line declares a variable `a` and assigns it the binary value `1010`.
- `let b = 0b1100;`: This line declares a variable `b` and assigns it the binary value `1100`.
- `let result = a ^ b;`: This line performs a bitwise exclusive OR operation on `a` and `b`, and assigns the result to the variable `result`.
- `println!("{:b}", result);`: This line prints the binary representation of the result of the bitwise exclusive OR operation.

## Helpful links
- [Rust Bitwise Operators](https://doc.rust-lang.org/book/ch03-02-operators.html#bitwise-operators)

group: rust-bitwise