# How to format a string with integer in Rust
// plain

Formatting a string with an integer in Rust is done using the `format!` macro. This macro takes a format string and a list of arguments and returns a `String` object. The format string contains placeholders for the arguments, which are replaced with the values of the arguments.

## Code example:

```
let x = 10;
let formatted_string = format!("The value of x is {}", x);
```

### Output

`The value of x is 10`

Explanation:

1. The `let` keyword is used to declare a variable `x` and assign it the value `10`.
2. The `format!` macro is used to create a `String` object from a format string and a list of arguments. In this case, the format string is `"The value of x is {}"` and the argument is `x`.
3. The `format!` macro replaces the placeholder `{}` in the format string with the value of the argument `x`, which is `10`.
4. The `format!` macro returns a `String` object with the value `The value of x is 10`.

## Helpful links:

1. [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
2. [Rust by Example - format!](https://doc.rust-lang.org/rust-by-example/macros/format.html)