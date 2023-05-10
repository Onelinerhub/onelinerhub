# How do I format a variable in Rust?
// plain

Formatting a variable in Rust is done using the `format!` macro. This macro takes a format string and a list of arguments, and returns a `String` containing the formatted text.

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

## Code explanation

- `format!`: The macro used to format a variable.
- `"My name is {}, and I am {} years old."`: The format string, which contains placeholders for the arguments.
- `name` and `age`: The arguments that will be used to fill in the placeholders.
- `println!`: The macro used to print the formatted string.

## Helpful links
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust Documentation - println!](https://doc.rust-lang.org/std/macro.println.html)

group: rust-variables