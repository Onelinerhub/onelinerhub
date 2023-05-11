# How to match the end of a line in a Rust regex?
// plain

To match the end of a line in a Rust regex, use the `$` character. This character matches the end of a line, regardless of the line ending character. For example:

```rust
let re = Regex::new(r"end$").unwrap();
assert!(re.is_match("This is the end"));
assert!(!re.is_match("This is not the end."));
```

The code above creates a new regex object with the pattern `end$`. The `$` character at the end of the pattern indicates that the pattern should match the end of the line. The code then tests two strings to see if they match the pattern. The first string, `This is the end`, matches the pattern because it ends with `end`. The second string, `This is not the end.`, does not match the pattern because it does not end with `end`.

Parts of the code:

- `Regex::new(r"end$")`: creates a new regex object with the pattern `end$`
- `assert!(re.is_match("This is the end"))`: tests if the string `This is the end` matches the pattern `end$`
- `assert!(!re.is_match("This is not the end."))`: tests if the string `This is not the end.` matches the pattern `end$`

## Helpful links

- [Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Regex Syntax](https://doc.rust-lang.org/regex/regex/index.html#syntax)

group: rust-regex

onelinerhub: [How to match the end of a line in a Rust regex?](https://onelinerhub.com/rust/how-to-match-the-end-of-a-line-in-a-rust-regex)