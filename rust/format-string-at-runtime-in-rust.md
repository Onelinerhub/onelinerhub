# Format string at runtime in Rust
// plain

Formatting strings at runtime in Rust can be done using the `format!` macro. This macro allows you to create a formatted string using the same syntax as `println!` and `print!`.

Example:
```
let name = "John";
let age = 30;

println!("{} is {} years old", name, age);
// ### Output John is 30 years old
```

Explanation:
- `let name = "John";`: This line declares a variable `name` and assigns it the value `"John"`.
- `let age = 30;`: This line declares a variable `age` and assigns it the value `30`.
- `println!("{} is {} years old", name, age);`: This line uses the `println!` macro to print a formatted string. The `{}` are placeholders for the values of `name` and `age` which are passed as arguments to the macro.

### Output
John is 30 years old

## Helpful links:
- [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
- [Rust Documentation - Formatting](https://doc.rust-lang.org/std/fmt/)