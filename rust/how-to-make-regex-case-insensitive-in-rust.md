# How to make regex case insensitive in Rust?
// plain

To make regex case insensitive in Rust, you can use the `i` flag. This flag can be added to the end of the regex pattern. For example:

```rust
let re = Regex::new(r"(?i)hello").unwrap();
```

This will create a case insensitive regex pattern that will match both `hello` and `HELLO`.

## Code explanation


- `Regex::new`: This is a function that creates a new Regex object.
- `r"(?i)hello"`: This is the regex pattern. The `(?i)` flag makes the pattern case insensitive.
- `unwrap`: This is a method that will return the Regex object if the pattern is valid, or panic if the pattern is invalid.

## Helpful links

- [Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Regex Flags](https://doc.rust-lang.org/regex/regex/enum.Flags.html)

group: rust-regex

onelinerhub: [How to make regex case insensitive in Rust?](https://onelinerhub.com/rust/how-to-make-regex-case-insensitive-in-rust)