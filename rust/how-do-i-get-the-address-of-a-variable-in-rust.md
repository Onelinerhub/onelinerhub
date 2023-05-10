# How do I get the address of a variable in Rust?
// plain

You can get the address of a variable in Rust using the `&` operator. For example:

```
let x = 5;
let address = &x;
println!("The address of x is: {:p}", address);
```

## Output example

```
The address of x is: 0x7ffd7f9f3fec
```

The code above consists of the following parts:

1. `let x = 5;` - This declares a variable `x` with the value `5`.
2. `let address = &x;` - This declares a variable `address` and assigns it the address of `x` using the `&` operator.
3. `println!("The address of x is: {:p}", address);` - This prints the address of `x` using the `{:p}` format specifier.

## Helpful links

- [Rust Reference - The `&` Operator](https://doc.rust-lang.org/reference/operators/index.html#the-ampersand-operator)
- [Rust Reference - Formatting](https://doc.rust-lang.org/std/fmt/index.html#formatting)

group: rust-variables