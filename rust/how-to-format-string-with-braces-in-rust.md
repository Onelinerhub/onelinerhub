# How to format string with braces in Rust
// plain

String formatting in Rust is done using the `format!` macro. This macro allows you to insert values into a string using braces `{}` as placeholders.

Example:
```rust
let name = "John";
let age = 30;
println!("My name is {}, and I am {} years old.", name, age);
```
### Output
My name is John, and I am 30 years old.

Explanation:
1. The `format!` macro is used to format strings in Rust.
2. The `{}` braces are used as placeholders for values that will be inserted into the string.
3. The values to be inserted into the string are passed as arguments to the `format!` macro.
4. The `println!` macro is used to print the formatted string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/std/macro.println.html