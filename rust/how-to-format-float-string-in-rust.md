# How to format float string in Rust
// plain

Formatting a float string in Rust can be done using the `format!` macro. This macro takes a format string and a list of arguments and returns a `String` object. The format string can contain special formatting characters that will be replaced with the corresponding argument.

For example, to format a float string with two decimal places, the following code can be used:

```rust
let x = 3.14159;
let formatted_string = format!("{:.2}", x);
println!("{}", formatted_string);
```

### Output
3.14

Explanation:
1. The `let x = 3.14159` statement declares a variable `x` and assigns it the value `3.14159`.
2. The `let formatted_string = format!("{:.2}", x)` statement uses the `format!` macro to create a `String` object with the value `3.14` from the float `x`. The `{:.2}` part of the format string specifies that the float should be formatted with two decimal places.
3. The `println!("{}", formatted_string)` statement prints the formatted string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/std/fmt/index.html