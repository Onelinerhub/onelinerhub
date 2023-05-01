# How to format string in Rust
// plain

String formatting in Rust is done using the `format!` macro. This macro allows you to create a formatted string with placeholders for values that will be filled in later.

## Code example:
```
let name = "John";
let age = 30;

println!("{} is {} years old", name, age);
```
### Output
John is 30 years old

## Explanation of code parts:
1. `let name = "John";` - This line declares a variable called `name` and assigns it the value of "John".
2. `let age = 30;` - This line declares a variable called `age` and assigns it the value of 30.
3. `println!("{} is {} years old", name, age);` - This line uses the `format!` macro to print out a formatted string with the values of `name` and `age` in the appropriate places.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/rust-by-example/macros/format.html