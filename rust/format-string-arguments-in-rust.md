# Format string arguments in Rust
// plain

?



Formatting string arguments in Rust is done using the `format!` macro. This macro takes a format string and a list of arguments and returns a `String` object. The format string can contain placeholders for the arguments, which are then replaced with the corresponding values.

## Code example:

```
let name = "John";
let age = 30;
let message = format!("Hello, my name is {}, and I am {} years old.", name, age);
println!("{}", message);
```

### Output

Hello, my name is John, and I am 30 years old.

## Explanation of Code Parts:

1. `let name = "John";` - This line declares a variable called `name` and assigns it the value of the string `"John"`.
2. `let age = 30;` - This line declares a variable called `age` and assigns it the value of the integer `30`.
3. `let message = format!("Hello, my name is {}, and I am {} years old.", name, age);` - This line uses the `format!` macro to create a `String` object called `message`. The format string contains two placeholders, `{}`, which are replaced with the values of the variables `name` and `age`.
4. `println!("{}", message);` - This line prints the value of the `message` variable to the console.

## Helpful links:

1. [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
2. [Rust by Example - format!](https://doc.rust-lang.org/rust-by-example/macros/format.html)