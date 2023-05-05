# How do I convert a string to a str in Rust?
// plain

To convert a string to a str in Rust, you can use the `to_string()` method. This method will convert a string to a str type.

## Example

```
let my_string = "Hello World!";
let my_str = my_string.to_string();
println!("{}", my_str);
```
## Output example

```
Hello World!
```

The `to_string()` method takes a string as an argument and returns a str type. The str type is a string type that is immutable and can be used for various operations.

## Code explanation

- `let my_string = "Hello World!";`: This line declares a variable `my_string` and assigns it the value of a string literal.
- `let my_str = my_string.to_string();`: This line calls the `to_string()` method on the `my_string` variable and assigns the result to the `my_str` variable.
- `println!("{}", my_str);`: This line prints the value of the `my_str` variable to the console.

## Helpful links
- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust String Conversion](https://doc.rust-lang.org/std/string/struct.String.html#method.to_string)