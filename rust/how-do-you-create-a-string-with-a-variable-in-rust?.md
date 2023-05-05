# How do you create a string with a variable in Rust?
// plain

Creating a string with a variable in Rust is a simple process. To do this, you must first declare a variable and assign it a value. Then, you can use the `format!` macro to create a string with the variable.

```rust
let my_variable = "Hello World";
let my_string = format!("This is my variable: {}", my_variable);
println!("{}", my_string);
```

## Output example

```
This is my variable: Hello World
```

The code above consists of three parts:

1. `let my_variable = "Hello World";` - This declares a variable called `my_variable` and assigns it the value `"Hello World"`.
2. `let my_string = format!("This is my variable: {}", my_variable);` - This uses the `format!` macro to create a string with the value of `my_variable` inserted into it. The `{}` is a placeholder for the variable.
3. `println!("{}", my_string);` - This prints the string to the console.

## Helpful links

- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)