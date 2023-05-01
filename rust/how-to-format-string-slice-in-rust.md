# How to format string slice in Rust
// plain

String slices in Rust can be formatted using the `format!` macro. This macro takes a format string and a list of arguments and returns a `String` object. The format string can contain placeholders for the arguments, which are then replaced with the corresponding values.

## Code example:
```
let name = "John";
let age = 30;
let formatted_string = format!("My name is {}, and I am {} years old.", name, age);
```

### Output
`My name is John, and I am 30 years old.`

## Explanation of code parts:
1. `let name = "John";` - This line declares a variable `name` and assigns it the value `"John"`, which is a string literal.
2. `let age = 30;` - This line declares a variable `age` and assigns it the value `30`, which is an integer literal.
3. `let formatted_string = format!("My name is {}, and I am {} years old.", name, age);` - This line uses the `format!` macro to create a `String` object from the format string `"My name is {}, and I am {} years old."` and the variables `name` and `age`. The placeholders `{}` in the format string are replaced with the values of the variables `name` and `age`.

## Helpful links:
1. [Rust Documentation - format! macro](https://doc.rust-lang.org/std/macro.format.html)
2. [Rust by Example - format! macro](https://doc.rust-lang.org/rust-by-example/macros/format.html)