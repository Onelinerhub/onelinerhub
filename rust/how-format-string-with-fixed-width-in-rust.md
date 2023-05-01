# How format string with fixed width in Rust
// plain

Formatting strings with fixed width in Rust can be done using the `format!` macro. This macro allows you to specify the width of the string, as well as other formatting options.

## Code example:
```
let name = "John";
let formatted_name = format!("{:10}", name);
println!("{}", formatted_name);
```
### Output
John

## Explanation of code parts:
1. `let name = "John"`: This line declares a variable called `name` and assigns it the value of "John".
2. `let formatted_name = format!("{:10}", name)`: This line uses the `format!` macro to format the `name` variable with a width of 10 characters.
3. `println!("{}", formatted_name)`: This line prints the formatted string to the console.

## Helpful links:
1. [Rust Documentation - Formatting Strings](https://doc.rust-lang.org/std/fmt/index.html#formatting-strings)
2. [Rust by Example - Formatting](https://doc.rust-lang.org/rust-by-example/fmt/format.html)