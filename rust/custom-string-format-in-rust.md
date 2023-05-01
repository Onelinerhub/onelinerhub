# Custom string format in Rust
// plain

Rust provides a powerful formatting system for strings, called `format!`. It allows you to create strings with dynamic content, and is used in a similar way to `println!`.

Here is an example of using `format!` to create a string with dynamic content:

```rust
let name = "John";
let age = 30;

let message = format!("Hello, my name is {}, and I am {} years old.", name, age);
println!("{}", message);
```
### Output
Hello, my name is John, and I am 30 years old.

## Explanation of code parts:
1. `let name = "John";` - This line declares a variable called `name` and assigns it the value of "John".
2. `let age = 30;` - This line declares a variable called `age` and assigns it the value of 30.
3. `let message = format!("Hello, my name is {}, and I am {} years old.", name, age);` - This line uses the `format!` macro to create a string with dynamic content. The `{}` symbols are placeholders for the values of the `name` and `age` variables.
4. `println!("{}", message);` - This line prints the `message` string to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/macro.format.html
2. https://doc.rust-lang.org/book/ch08-02-formatting-strings.html