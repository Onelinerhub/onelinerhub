# Bitwise OR operator usage in Rust
// plain

The bitwise OR operator (`|`) is a binary operator in Rust that performs a bitwise OR operation on two operands. It is used to set bits in a binary number, or to combine two binary numbers.

## Example

```
let a = 0b1010;
let b = 0b1100;
let c = a | b;
```
## Output example

```
c = 0b1110
```

The code above sets the variable `a` to the binary number `1010`, the variable `b` to the binary number `1100`, and the variable `c` to the result of the bitwise OR operation between `a` and `b`, which is `1110`.

The bitwise OR operator can also be used to combine two binary numbers. For example:

```
let a = 0b1010;
let b = 0b1100;
let c = a | b;
```

## Output example

```
c = 0b1110
```

In this example, the bitwise OR operation combines the binary numbers `1010` and `1100` to produce the binary number `1110`.

## Helpful links

- [Rust Bitwise Operators](https://doc.rust-lang.org/book/ch03-02-operators.html#bitwise-operators)
- [Rust Bitwise OR Operator](https://www.tutorialspoint.com/rust/rust_bitwise_or_operator.htm)

group: rust-bitwise