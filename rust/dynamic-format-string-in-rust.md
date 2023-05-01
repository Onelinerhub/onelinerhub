# Dynamic format string in Rust
// plain

Format strings in Rust are used to create formatted strings from a template string and a set of arguments. The format string can be a static string or a dynamic string.

A dynamic format string is a string that is created at runtime, rather than being hard-coded into the program. This allows for more flexibility in the formatting of the output string.

The following ## Code example shows how to create a dynamic format string in Rust:

```rust
let template_string = "The number is {}";
let number = 5;
let dynamic_string = format!(template_string, number);
println!("{}", dynamic_string);
```

### Output
The number is 5

Explanation:
1. The `let template_string = "The number is {}";` line creates a template string with a placeholder for the number.
2. The `let number = 5;` line creates a variable to store the number.
3. The `let dynamic_string = format!(template_string, number);` line uses the `format!` macro to create a dynamic string from the template string and the number.
4. The `println!("{}", dynamic_string);` line prints the dynamic string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/rust-by-example/macros/format.html