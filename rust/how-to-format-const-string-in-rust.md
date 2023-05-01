# How to format const string in Rust
// plain

Rust provides a number of ways to format const strings. The most common way is to use the `format!` macro. This macro takes a format string and a list of arguments and returns a `String` object.

## Code example:
```
let name = "John";
let age = 30;
let formatted_string = format!("My name is {}, and I am {} years old.", name, age);
println!("{}", formatted_string);
```

### Output
My name is John, and I am 30 years old.

## Explanation:
1. The `format!` macro takes a format string and a list of arguments and returns a `String` object.
2. The format string is a string literal that contains placeholders for the arguments. The placeholders are surrounded by curly braces `{}`.
3. The arguments are passed after the format string and are separated by commas.
4. The `println!` macro is used to print the formatted string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/std/macro.println.html