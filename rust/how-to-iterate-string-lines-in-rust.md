# How to iterate string lines in Rust
// plain

Iterating over string lines in Rust can be done using the `lines()` method on a `String` type. This method returns an iterator over the lines of the string.

## Example code

```rust
let text = "Hello
World";

for line in text.lines() {
    println!("{}", line);
}
```

## Output example

```
Hello
World
```

## Code explanation

- `let text = "Hello\nWorld";`: This creates a `String` type with two lines.
- `for line in text.lines()`: This creates an iterator over the lines of the `text` string.
- `println!("{}", line);`: This prints each line of the `text` string.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)

group: rust-loops