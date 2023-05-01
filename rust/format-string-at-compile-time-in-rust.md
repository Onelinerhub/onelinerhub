# Format string at compile time in Rust
// plain

Format strings in Rust can be compiled at compile time using the `format!` macro. This macro takes a format string as its first argument, followed by any number of arguments that will be used to fill in the format string. The format string can contain placeholders for the arguments, which are denoted by curly braces `{}`.

## Code example:
```
let name = "John";
let age = 30;
let message = format!("Hello, my name is {}, and I am {} years old.", name, age);
println!("{}", message);
```
### Output
Hello, my name is John, and I am 30 years old.

## Explanation of code parts:
1. `let name = "John";` - This line declares a variable `name` and assigns it the value of the string `John`.
2. `let age = 30;` - This line declares a variable `age` and assigns it the value of the integer `30`.
3. `let message = format!("Hello, my name is {}, and I am {} years old.", name, age);` - This line uses the `format!` macro to create a string with the given format string and arguments. The placeholders `{}` are replaced with the values of the variables `name` and `age`.
4. `println!("{}", message);` - This line prints the value of the `message` variable to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/rust-by-example/macros/format.html