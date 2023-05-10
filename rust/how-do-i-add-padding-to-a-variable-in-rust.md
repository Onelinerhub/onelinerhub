# How do I add padding to a variable in Rust?
// plain

Adding padding to a variable in Rust is done using the `format!` macro. This macro allows you to specify the width of the output and the character to use for padding. For example, the following code will pad a variable with spaces to a width of 10 characters:

```rust
let x = 5;
let padded = format!("{:10}", x);
println!("{}", padded);
```

## Output example

```
     5
```

## Code explanation

- `format!`: The macro used to add padding to a variable.
- `{:10}`: The formatting syntax used to specify the width of the output and the character to use for padding.
- `x`: The variable to be padded.
- `padded`: The variable containing the padded output.
- `println!`: The macro used to print the padded output.

## Helpful links
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust Documentation - println!](https://doc.rust-lang.org/std/macro.println.html)

group: rust-variables