# How to match all using regex in Rust?
// plain

Regex (regular expressions) in Rust can be used to match patterns in strings. To match all using regex, the `Regex::new()` method can be used. This method takes a string as an argument and returns a `Regex` object.

## Example code

```rust
let re = Regex::new(r"\d+").unwrap();
```

## Output example

```
Regex
```

## Code explanation

- `Regex::new()`: This method takes a string as an argument and returns a `Regex` object.
- `r"\d+"`: This is the regex pattern that will be used to match all strings.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to match all using regex in Rust?](https://onelinerhub.com/rust/how-to-match-all-using-regex-in-rust)