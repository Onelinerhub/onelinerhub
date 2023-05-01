# How to use variables in string while formatting in Rust
// plain

Variables can be used in string formatting in Rust using the `format!` macro. The `format!` macro takes a format string as its first argument, followed by the variables to be used in the format string. The format string is a string literal that contains placeholders for the variables. The placeholders are written in curly braces `{}` and are replaced by the variables when the `format!` macro is called.

For example, the following code:

```
let name = "John";
let age = 30;

println!("{} is {} years old", name, age);
```

will ### Output

`John is 30 years old`

The code can be broken down as follows:

1. Two variables, `name` and `age`, are declared and assigned values.
2. The `format!` macro is called with the format string `"{} is {} years old"` as its first argument, followed by the variables `name` and `age`.
3. The `format!` macro replaces the placeholders `{}` in the format string with the values of the variables `name` and `age`.
4. The resulting string is printed to the console using the `println!` macro.

For more information, see the [Rust documentation on string formatting](https://doc.rust-lang.org/std/fmt/) and the [Rust by Example guide on string formatting](https://doc.rust-lang.org/rust-by-example/std_misc/format.html).