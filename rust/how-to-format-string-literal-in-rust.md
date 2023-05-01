# How to format string literal in Rust
// plain

String literals in Rust can be formatted using the `format!` macro. This macro allows you to insert variables into a string literal and format them according to the specified format.

## Code example:
```
let name = "John";
let age = 30;
println!("{} is {} years old", name, age);
```

### Output
John is 30 years old

Explanation:
- `let name = "John";`: This line declares a variable `name` and assigns it the value `"John"`.
- `let age = 30;`: This line declares a variable `age` and assigns it the value `30`.
- `println!("{} is {} years old", name, age);`: This line uses the `format!` macro to print out a string literal with the variables `name` and `age` inserted into it. The `{}` symbols indicate where the variables should be inserted.

## Helpful links:
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust by Example - format!](https://doc.rust-lang.org/rust-by-example/macros/format.html)