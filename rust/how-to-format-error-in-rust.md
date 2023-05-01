# How to format error in Rust
// plain

Rust provides a number of ways to format errors. The most common way is to use the `format!` macro. This macro allows you to create a formatted string from a template and a list of arguments.

## Code example:
```
let name = "John";
let age = 30;
let error = format!("{} is {} years old", name, age);
println!("{}", error);
```

### Output
John is 30 years old

Explanation:
1. The `format!` macro takes a template string and a list of arguments.
2. The template string is a string literal that contains placeholders for the arguments.
3. The placeholders are denoted by curly braces `{}` and the arguments are passed in the same order as the placeholders.
4. The `println!` macro is used to print the formatted string to the console.

## Helpful links:
1. [Rust Documentation - Formatting](https://doc.rust-lang.org/std/fmt/)
2. [Rust by Example - Formatting](https://doc.rust-lang.org/rust-by-example/fmt/format.html)