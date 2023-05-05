# How do you match strings with regex in Rust?
// plain

Matching strings with regex in Rust is done using the `regex` crate. This crate provides a `Regex` type which can be used to match strings against a regular expression.

## Example code

```rust
use regex::Regex;

let re = Regex::new(r"^\d{4}-\d{2}-\d{2}$").unwrap();
assert!(re.is_match("2018-01-01"));
```

## Output example

```
(no output)
```

## Code explanation

- `use regex::Regex`: imports the `Regex` type from the `regex` crate.
- `Regex::new(r"^\d{4}-\d{2}-\d{2}$")`: creates a new `Regex` object from the given regular expression.
- `.unwrap()`: unwraps the `Result` returned by `Regex::new` and panics if the regular expression is invalid.
- `re.is_match("2018-01-01")`: checks if the given string matches the regular expression.

## Helpful links
- [Regex crate documentation](https://docs.rs/regex/1.3.1/regex/)