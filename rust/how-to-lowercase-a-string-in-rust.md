# How to lowercase a string in Rust
// plain

You can lowercase a string in Rust using the `to_lowercase()` method.

Example code:
```
let my_string = "HELLO WORLD";
let lowercase_string = my_string.to_lowercase();
println!("{}", lowercase_string);
```
### Output
```
hello world
```
Explanation:
- `let my_string = "HELLO WORLD";`: This line declares a variable `my_string` and assigns it the value of the string `"HELLO WORLD"`.
- `let lowercase_string = my_string.to_lowercase();`: This line calls the `to_lowercase()` method on the `my_string` variable, which returns a new string with all characters in lowercase. This new string is then assigned to the `lowercase_string` variable.
- `println!("{}", lowercase_string);`: This line prints the value of the `lowercase_string` variable to the console.

## Helpful links:
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - to_lowercase()](https://doc.rust-lang.org/std/primitive.str.html#method.to_lowercase)