# How to format multiline string in Rust
// plain

In Rust, you can format multiline strings using the `format!` macro. This macro allows you to create a string with placeholders that can be replaced with values.

## Code example:
```
let name = "John";
let age = 30;

let multiline_string = format!("My name is {},
I am {} years old.", name, age);

println!("{}", multiline_string);
```
### Output
```
My name is John,
I am 30 years old.
```

## Explanation of code parts:
1. `let name = "John";`: This line declares a variable `name` and assigns it the value `"John"`.
2. `let age = 30;`: This line declares a variable `age` and assigns it the value `30`.
3. `let multiline_string = format!("My name is {}, I am {} years old.", name, age);`: This line uses the `format!` macro to create a multiline string with placeholders for the values of `name` and `age`.
4. `println!("{}", multiline_string);`: This line prints the multiline string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/rust-by-example/macros/format.html