# How to format string with println in Rust
// plain

Rust provides a number of ways to format strings with the println! macro. The most basic way is to use the placeholder syntax, which allows you to insert values into the string. The placeholder syntax uses curly braces `{}` to indicate where the value should be inserted.

For example, the following code will print out the string "Hello, world!" with the value of the variable `name` inserted into the string:

```
let name = "world";
println!("Hello, {}!", name);
```
### Output
Hello, world!

## Explanation of code parts:
1. `let name = "world";` - This line declares a variable called `name` and assigns it the value of "world".
2. `println!("Hello, {}!", name);` - This line uses the println! macro to print out the string "Hello, world!" with the value of the `name` variable inserted into the string. The `{}` indicates where the value of the `name` variable should be inserted.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.println.html
2. https://doc.rust-lang.org/rust-by-example/macros/print.html