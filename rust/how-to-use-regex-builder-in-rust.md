# How to use regex builder in Rust?
// plain

Regex builder in Rust is a powerful tool for creating regular expressions. It allows you to quickly and easily create complex regular expressions.

## Example code

```rust
let re = RegexBuilder::new(r"\d{4}-\d{2}-\d{2}")
    .case_insensitive(true)
    .build()
    .unwrap();
```

## Output example

```
Regex(r"\d{4}-\d{2}-\d{2}", CaseInsensitive(true))
```

The code above creates a regular expression that matches a date in the format of YYYY-MM-DD, and is case insensitive.

The code consists of the following parts:

- `RegexBuilder::new(r"\d{4}-\d{2}-\d{2}")` creates a new RegexBuilder object with the regular expression pattern.
- `case_insensitive(true)` sets the regular expression to be case insensitive.
- `build()` builds the regular expression.
- `unwrap()` unwraps the result of the build, returning the Regex object.

## Helpful links

- [The Rust Regex Guide](https://doc.rust-lang.org/regex/index.html)
- [The Rust Regex Cheatsheet](https://cheats.rs/)

group: rust-regex

onelinerhub: [How to use regex builder in Rust?](https://onelinerhub.com/rust/how-to-use-regex-builder-in-rust)