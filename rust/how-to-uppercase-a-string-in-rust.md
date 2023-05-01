# How to uppercase a string in Rust
// plain

You can uppercase a string in Rust using the `to_uppercase()` method. Here is an example:

```
let my_string = "hello world";
let uppercase_string = my_string.to_uppercase();
println!("{}", uppercase_string);
```
### Output
```
HELLO WORLD
```

Explanation:
- `let my_string = "hello world";`: This line declares a variable `my_string` and assigns it the value of the string `"hello world"`.
- `let uppercase_string = my_string.to_uppercase();`: This line calls the `to_uppercase()` method on the `my_string` variable, and assigns the result to the `uppercase_string` variable.
- `println!("{}", uppercase_string);`: This line prints the value of the `uppercase_string` variable to the console.

## Helpful links:
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/primitive.str.html)
- [Rust Documentation - to_uppercase()](https://doc.rust-lang.org/std/primitive.str.html#method.to_uppercase)