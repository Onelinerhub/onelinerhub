# How can I create a string of repeated characters in Rust?
// plain

You can create a string of repeated characters in Rust using the `repeat()` method. This method takes a `char` and an `usize` as arguments and returns a `String` with the character repeated the specified number of times.

## Example code

```rust
let repeated_char = '*'.repeat(10);
println!("{}", repeated_char);
```

## Output example

```
**********
```

## Code explanation

- `let repeated_char = '*'`: declares a variable `repeated_char` and assigns it the character `*`
- `.repeat(10)`: calls the `repeat()` method on the character `*` and passes in the argument `10`
- `println!("{}", repeated_char)`: prints the value of the `repeated_char` variable to the console

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)