# How to get a capture group using Rust regex?
// plain

Capture groups are used to extract parts of a string that match a regular expression pattern. In Rust, capture groups are created using the `capture_group` method of the `Regex` struct.

## Example code

```rust
let re = Regex::new(r"(\d{4})-(\d{2})-(\d{2})").unwrap();
let caps = re.capture_group("2020-01-01").unwrap();
```

## Output example

```
[("2020-01-01", "2020", "01", "01")]
```

## Code explanation

- `Regex::new(r"(\d{4})-(\d{2})-(\d{2})")`: creates a new `Regex` struct with a regular expression pattern that matches a 4-digit year, followed by a 2-digit month, followed by a 2-digit day.
- `capture_group("2020-01-01")`: uses the `Regex` struct to capture the parts of the string that match the regular expression pattern.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to get a capture group using Rust regex?](https://onelinerhub.com/rust/how-to-get-a-capture-group-using-rust-regex)