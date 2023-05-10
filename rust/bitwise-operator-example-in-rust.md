# Bitwise operator example in Rust
// plain

Bitwise operators are used to perform bit-level operations on integer values in Rust. They are used to manipulate individual bits within a number.

## Example code

```
let x = 0b1010_1010;
let y = 0b0101_0101;

let result = x & y;
println!("{:b}", result);
```

## Output example

```
1010_0000
```

The code above uses the bitwise AND operator (`&`) to perform a bitwise operation on two numbers. The `x` variable is set to `1010_1010` in binary, and the `y` variable is set to `0101_0101` in binary. The `&` operator then performs a bitwise AND operation on the two numbers, resulting in `1010_0000`.

## Code explanation

- `let x = 0b1010_1010;`: This line declares a variable `x` and sets it to `1010_1010` in binary.
- `let y = 0b0101_0101;`: This line declares a variable `y` and sets it to `0101_0101` in binary.
- `let result = x & y;`: This line uses the bitwise AND operator (`&`) to perform a bitwise operation on the two numbers.
- `println!("{:b}", result);`: This line prints the result of the bitwise operation in binary format.

## Helpful links
- [Rust Bitwise Operators](https://doc.rust-lang.org/book/ch03-02-operators.html#bitwise-operators)
- [Rust Bitwise Operators Tutorial](https://www.tutorialspoint.com/rust/rust_bitwise_operators.htm)

group: rust-bitwise