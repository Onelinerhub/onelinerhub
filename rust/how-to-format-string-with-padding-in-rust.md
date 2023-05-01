# How to format string with padding in Rust
// plain

String padding in Rust can be done using the `format!` macro. The `format!` macro takes a format string and a list of arguments and returns a `String` object. The format string can contain special formatting characters that will be replaced with the corresponding argument.

For example, to pad a string with spaces, the `{:width$}` format can be used. The `width` argument specifies the total width of the output string, and the `$` character indicates that the padding should be done with spaces.

## Code example:
```
let s = "Hello";
let padded = format!("{:10$}", s, 10);
println!("{}", padded);
```
### Output
```
Hello
```
## Explanation of code parts:
1. `let s = "Hello";` - This line declares a variable `s` and assigns it the value `"Hello"`.
2. `let padded = format!("{:10$}", s, 10);` - This line uses the `format!` macro to format the string `s` with padding. The `{:10$}` format indicates that the output string should have a total width of 10 characters, and the padding should be done with spaces.
3. `println!("{}", padded);` - This line prints the padded string to the console.

## Helpful links:
1. [Rust Documentation - Formatting Strings](https://doc.rust-lang.org/std/fmt/index.html#formatting-strings)
2. [Rust by Example - Formatting](https://doc.rust-lang.org/rust-by-example/fmt/format.html)