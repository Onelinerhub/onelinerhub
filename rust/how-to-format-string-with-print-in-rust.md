# How to format string with print in Rust
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
3. `println!("{} is {} years old", name, age);` - This line uses the `format!` macro to print out a string with placeholders for the values of `name` and `age`. The values of `name` and `age` are then filled in when the string is printed.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html