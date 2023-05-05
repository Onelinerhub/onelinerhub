# How do you format a Rust string?
// plain

Rust strings are immutable and stored as UTF-8 encoded data. To format a Rust string, you can use the `format!` macro. This macro takes a format string and a list of arguments, and returns a `String` object.

```rust
let name = "John";
let age = 30;
let formatted_string = format!("My name is {}, and I am {} years old.", name, age);
println!("{}", formatted_string);
```

## Output example

```
My name is John, and I am 30 years old.
```

The `format!` macro works by taking a format string and a list of arguments. The format string contains placeholders for the arguments, which are replaced with the values of the arguments when the macro is evaluated. The placeholders are written in the form `{}`, and the arguments are separated by commas.

The list of arguments can contain any type of value, including strings, numbers, and boolean values. The values are automatically converted to strings when they are inserted into the format string.

## Helpful links

- [Rust Documentation - Formatting](https://doc.rust-lang.org/std/fmt/)
- [Rust by Example - Formatting](https://doc.rust-lang.org/rust-by-example/std_misc/format.html)