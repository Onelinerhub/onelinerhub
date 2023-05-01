# String interpolation in Rust
// plain

String interpolation in Rust is a way to create a string from a combination of literals, variables, and other expressions. It is done using the `format!` macro. The `format!` macro takes a format string as its first argument, followed by a comma-separated list of arguments. The format string contains placeholders for the arguments, which are replaced with the values of the arguments when the macro is evaluated.

## Code example:
```
let name = "John";
let age = 30;

println!("{} is {} years old", name, age);
```

### Output
John is 30 years old

## Explanation of code parts:
1. `let name = "John";` - This line declares a variable called `name` and assigns it the value of the string `"John"`.
2. `let age = 30;` - This line declares a variable called `age` and assigns it the value of the integer `30`.
3. `println!("{} is {} years old", name, age);` - This line uses the `format!` macro to create a string from the format string `"{} is {} years old"` and the variables `name` and `age`. The placeholders `{}` in the format string are replaced with the values of the variables `name` and `age`, resulting in the string `"John is 30 years old"` being printed to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/rust-by-example/macros/format.html