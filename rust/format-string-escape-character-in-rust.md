# Format string escape character in Rust
// plain

In Rust, the escape character for formatting strings is the backslash (`\`). This character is used to escape certain characters in a string, such as quotation marks, newlines, and other special characters. For example, the following code will print out the string "Hello, World!":

```
let my_string = "Hello, World!";
println!("{}", my_string);
```

### Output

Hello, World!

The backslash character is also used to insert special characters into a string, such as a newline character. For example, the following code will print out the string "Hello,

World!":

```
let my_string = "Hello,\nWorld!";
println!("{}", my_string);
```

### Output

Hello,
World!

## Explanation of code parts:

1. `let my_string = "Hello, World!";` - This line declares a variable called `my_string` and assigns it the value of the string "Hello, World!".

2. `println!("{}", my_string);` - This line uses the `println!` macro to print out the value of the `my_string` variable. The `{}` is a placeholder for the value of the `my_string` variable.

3. `let my_string = "Hello,\nWorld!";` - This line declares a variable called `my_string` and assigns it the value of the string "Hello,\nWorld!". The `\n` is an escape character that represents a newline character.

4. `println!("{}", my_string);` - This line uses the `println!` macro to print out the value of the `my_string` variable. The `{}` is a placeholder for the value of the `my_string` variable.

## Helpful links:

1. [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
2. [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)