# How to escape a Rust regex?
// plain

To escape a Rust regex, you can use the `\` character. This will tell the regex engine to treat the following character as a literal instead of a special character. For example, the following code will match the literal string `\d+`:

```rust
let re = Regex::new(r"\\d+").unwrap();
```

The code consists of the following parts:

- `Regex::new`: This is a function from the `regex` crate that creates a new `Regex` object.
- `r"\\d+"`: This is a raw string literal that contains the regex pattern. The `\` character is escaped with another `\` character, so that it is treated as a literal instead of a special character.
- `unwrap`: This is a method that is called on the `Regex` object to get the underlying `Regex` value.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to escape a Rust regex?](https://onelinerhub.com/rust/how-to-escape-a-rust-regex)