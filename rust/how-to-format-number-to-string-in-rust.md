# How to format number to string in Rust
// plain

Formatting a number to a string in Rust can be done using the `format!` macro. This macro takes a format string and a list of arguments and returns a `String` object. The format string can contain special formatting characters that will be replaced with the corresponding argument.

## Code example:
```
let num = 5;
let num_string = format!("The number is {}", num);
```

### Output
`The number is 5`

Explanation:
- `let num = 5;`: This line declares a variable `num` and assigns it the value `5`.
- `let num_string = format!("The number is {}", num);`: This line uses the `format!` macro to format the number `5` into a string. The `{}` in the format string is replaced with the value of `num`.
- The output of this code is `The number is 5`.

## Helpful links:
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust by Example - format!](https://doc.rust-lang.org/rust-by-example/macros/format.html)