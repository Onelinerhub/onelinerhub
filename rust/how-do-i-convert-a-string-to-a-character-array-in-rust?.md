# How do I convert a string to a character array in Rust?
// plain

To convert a string to a character array in Rust, you can use the `chars()` method. This method returns an iterator over the characters of a string. Here is an example:
```
let my_string = "Hello World";
let my_char_array: Vec<char> = my_string.chars().collect();
```
The output of this code will be a vector of characters: `['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']`.

## Code explanation

- `let my_string = "Hello World";`: This declares a string variable.
- `let my_char_array: Vec<char> = my_string.chars().collect();`: This uses the `chars()` method to convert the string to a character array, and stores it in a vector.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Iterators](https://doc.rust-lang.org/std/iter/index.html)