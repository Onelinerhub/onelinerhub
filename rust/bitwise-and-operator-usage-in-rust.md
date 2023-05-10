# Bitwise AND operator usage in Rust
// plain

The bitwise AND operator (`&`) is used in Rust to perform a bitwise AND operation on two values. This operation compares the bits of two values and returns a new value with the bits set to 1 only if both bits are 1.

## Example

```
let x = 0b1010;
let y = 0b1100;
let result = x & y;
```
## Output example

```
result = 0b1000
```

## Code explanation

- `let x = 0b1010;`: This line declares a variable `x` and assigns it the binary value `1010`.
- `let y = 0b1100;`: This line declares a variable `y` and assigns it the binary value `1100`.
- `let result = x & y;`: This line performs a bitwise AND operation on `x` and `y`, and assigns the result to the variable `result`.

## Helpful links
- [Rust Bitwise Operators](https://doc.rust-lang.org/book/ch03-02-operators.html#bitwise-operators)

group: rust-bitwise