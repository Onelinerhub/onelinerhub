# How do I check if a string is empty in Rust?
// plain

You can check if a string is empty in Rust by using the `is_empty()` method. This method returns a boolean value indicating whether the string is empty or not.

## Example code

```
let my_string = String::new();

if my_string.is_empty() {
    println!("String is empty");
}
```

## Output example

```
String is empty
```

## Code explanation

- `let my_string = String::new();`: This line creates a new empty string.
- `if my_string.is_empty()`: This line checks if the string is empty.
- `println!("String is empty");`: This line prints a message if the string is empty.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)