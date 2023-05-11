# How to match whitespace with a regex in Rust?
// plain

Matching whitespace with a regex in Rust is done using the `\s` character class. This character class matches any whitespace character, including spaces, tabs, and newlines.

```rust
let whitespace_regex = Regex::new(r"\s").unwrap();
let whitespace_string = "This string has whitespace!";

assert!(whitespace_regex.is_match(whitespace_string));
```

The code above will assert that the `whitespace_regex` matches the `whitespace_string`.

## Code explanation


- `let whitespace_regex = Regex::new(r"\s").unwrap();`: This line creates a new regex object using the `\s` character class.
- `let whitespace_string = "This string has whitespace!";`: This line creates a string that contains whitespace.
- `assert!(whitespace_regex.is_match(whitespace_string));`: This line asserts that the `whitespace_regex` matches the `whitespace_string`.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Rust Regex Character Classes](https://doc.rust-lang.org/regex/regex/enum.RegexSet.html#character-classes)

group: rust-regex

onelinerhub: [How to match whitespace with a regex in Rust?](https://onelinerhub.com/rust/how-to-match-whitespace-with-a-regex-in-rust)