# How do I check if a string contains a certain substring in Rust?
// plain

You can use the `contains()` method to check if a string contains a certain substring in Rust.

## Example

```
let my_string = "Hello World";

if my_string.contains("World") {
    println!("The string contains the substring!");
}
```
## Output example

```
The string contains the substring!
```

The `contains()` method takes a `&str` as an argument and returns a `bool` indicating whether the string contains the substring.

## Code explanation

- `let my_string = "Hello World";`: This declares a variable `my_string` and assigns it the value `"Hello World"`.
- `if my_string.contains("World") {`: This checks if the string `my_string` contains the substring `"World"`.
- `println!("The string contains the substring!");`: This prints the message `"The string contains the substring!"` if the string contains the substring.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)