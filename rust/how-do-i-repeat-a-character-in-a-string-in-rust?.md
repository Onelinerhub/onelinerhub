# How do I repeat a character in a string in Rust?
// plain

You can repeat a character in a string in Rust using the `repeat()` method. This method takes a single argument, which is the number of times the character should be repeated.

For example:
```
let repeated_char = "*".repeat(5);
println!("{}", repeated_char);
```
This will output:
```
*****
```

The `repeat()` method is part of the `std::string::String` type, and can be used on any string.

Parts of the code:
- `let repeated_char = "*".repeat(5);`: This line creates a new string, `repeated_char`, which is a string of 5 asterisks.
- `println!("{}", repeated_char);`: This line prints the string `repeated_char` to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)