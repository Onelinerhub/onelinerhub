# How to use binary regex in Rust?
// plain

Rust supports regular expressions through the `regex` crate. To use binary regex, you need to specify the `regex::bytes` module.

```rust
use regex::bytes::Regex;

let re = Regex::new(b"^[0-9]+$").unwrap();
assert!(re.is_match(b"12345"));
```

The code above creates a binary regex that matches any sequence of one or more digits. The `Regex::new` function takes a byte string as its argument and returns a `Regex` object. The `is_match` method is then used to check if the given byte string matches the regex.

- `use regex::bytes::Regex`: imports the `Regex` type from the `regex::bytes` module.
- `Regex::new(b"^[0-9]+$")`: creates a `Regex` object from the given byte string.
- `is_match(b"12345")`: checks if the given byte string matches the regex.

## Helpful links
- [Rust Regex Documentation](https://docs.rs/regex/1.3.9/regex/)
- [Rust Regex Bytes Documentation](https://docs.rs/regex/1.3.9/regex/bytes/index.html)

group: rust-regex

onelinerhub: [How to use binary regex in Rust?](https://onelinerhub.com/rust/how-to-use-binary-regex-in-rust)