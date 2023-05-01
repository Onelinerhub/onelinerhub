# How to format strings and truncate long ones in Rust
// plain

Formatting strings and truncating long ones in Rust can be done using the `format!` macro. This macro allows you to specify a format string and a list of arguments to be formatted according to the format string. The format string can contain placeholders for the arguments, which will be replaced with the corresponding argument values. Additionally, the `format!` macro can be used to truncate long strings by specifying a maximum length for the output string.

Below is an example of using the `format!` macro to format and truncate a string:

```
let long_string = "This is a very long string that needs to be truncated";
let truncated_string = format!("{:.10}", long_string);

println!("{}", truncated_string);
```

### Output

`This is a`

In the above example, the `format!` macro is used to format the `long_string` variable. The `{:.10}` part of the format string specifies that the output string should be truncated to a maximum length of 10 characters. The resulting truncated string is then printed using the `println!` macro.

## Explanation of code parts:
- `let long_string = "This is a very long string that needs to be truncated";`: This line declares a variable called `long_string` and assigns it a string value.
- `let truncated_string = format!("{:.10}", long_string);`: This line uses the `format!` macro to format the `long_string` variable. The `{:.10}` part of the format string specifies that the output string should be truncated to a maximum length of 10 characters.
- `println!("{}", truncated_string);`: This line prints the truncated string using the `println!` macro.

## Helpful links:
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust Documentation - println!](https://doc.rust-lang.org/std/macro.println.html)