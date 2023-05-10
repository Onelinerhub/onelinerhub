# How do I increment a variable in Rust?
// plain

Incrementing a variable in Rust is done using the `+=` operator. This operator adds the right-hand side of the equation to the left-hand side and assigns the result to the left-hand side.

## Example

```
let mut x = 5;
x += 1;
```
## Output example

```
6
```

The code above consists of three parts:
1. `let mut x = 5;` - This declares a mutable variable `x` and assigns it the value `5`.
2. `x += 1;` - This uses the `+=` operator to add `1` to `x` and assign the result to `x`.
3. `6` - This is the output of the code, which is the value of `x` after the `+=` operator is applied.

## Helpful links
- [Rust Documentation - Operators](https://doc.rust-lang.org/book/ch03-02-operators.html)

group: rust-variables