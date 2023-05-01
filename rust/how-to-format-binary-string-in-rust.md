# How to format binary string in Rust
// plain

Formatting a binary string in Rust can be done using the `format!` macro. This macro allows you to create a formatted string using the same syntax as `println!`.

Below is an example of how to format a binary string in Rust:

```
let binary_string = format!("{:b}", 10);
println!("{}", binary_string);
```
### Output
1010

Explanation:
1. The `format!` macro is used to create a formatted string.
2. The `{:b}` is used to specify that the string should be formatted as a binary string.
3. The number 10 is passed as an argument to the macro.
4. The formatted string is stored in the `binary_string` variable.
5. The `println!` macro is used to print the formatted string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/std/macro.println.html