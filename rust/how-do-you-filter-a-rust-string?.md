# How do you filter a Rust string?
// plain

Filtering a Rust string can be done using the `filter()` method. This method takes a closure as an argument and returns a new string with only the characters that satisfy the closure's condition.

## Example

```
let my_string = "Hello World!";
let filtered_string = my_string.filter(|c| c.is_alphabetic());
```
## Output example

```
HelloWorld
```

The code above filters the string `my_string` and stores the result in `filtered_string`. The closure passed to `filter()` checks if each character is alphabetic and only keeps those that are.

The parts of the code are:
- `let my_string = "Hello World!";`: This declares a string variable `my_string` and assigns it the value `"Hello World!"`.
- `let filtered_string = my_string.filter(|c| c.is_alphabetic());`: This declares a string variable `filtered_string` and assigns it the result of calling `filter()` on `my_string`. The closure passed to `filter()` checks if each character is alphabetic and only keeps those that are.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)