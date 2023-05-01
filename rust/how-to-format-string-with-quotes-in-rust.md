# How to format string with quotes in Rust
// plain

In Rust, you can format strings with quotes by using the `format!` macro. This macro allows you to insert variables into a string and format them as desired.

For example, the following code:

```
let name = "John";
let age = 30;
let message = format!("My name is \"{}\", and I am {} years old.", name, age);
println!("{}", message);
```

will ### Output

```
My name is "John", and I am 30 years old.
```

Explanation:
- The `format!` macro is used to format strings with variables.
- The `name` and `age` variables are declared and assigned values.
- The `message` variable is assigned the result of the `format!` macro, which inserts the `name` and `age` variables into the string and formats them with quotes.
- The `println!` macro is used to print the `message` variable to the console.

## Helpful links:
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust Documentation - println!](https://doc.rust-lang.org/std/macro.println.html)