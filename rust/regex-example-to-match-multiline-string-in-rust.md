# Regex example to match multiline string in Rust?
// plain

Regex (Regular Expressions) is a powerful tool for matching patterns in strings. In Rust, the `regex` crate provides a library for creating and using regular expressions.

The following example shows how to match a multiline string in Rust using the `regex` crate:

```rust
use regex::Regex;

let re = Regex::new(r"(?m)^.*$").unwrap();
let text = "This is
a multiline
string";

for line in re.captures_iter(text) {
    println!("{}", line[0]);
}
```

## Output example

```
This is
a multiline
string
```

The code consists of the following parts:

1. `use regex::Regex;`: This imports the `Regex` type from the `regex` crate.
2. `let re = Regex::new(r"(?m)^.*$").unwrap();`: This creates a new `Regex` object from the given pattern. The `(?m)` flag enables multiline mode, which allows the pattern to match across multiple lines. The `^.*$` pattern matches any line of text.
3. `let text = "This is
a multiline
string";`: This creates a string containing multiple lines of text.
4. `for line in re.captures_iter(text) {`: This iterates over all the lines in the text, capturing each line in a `Captures` object.
5. `println!("{}", line[0]);`: This prints the captured line.

## Helpful links

- [Rust Regex Documentation](https://docs.rs/regex/1.3.9/regex/)
- [Regular-Expressions.info - Multiline Mode](https://www.regular-expressions.info/modifiers.html#multiline)

group: rust-regex

onelinerhub: [Regex example to match multiline string in Rust?](https://onelinerhub.com/rust/regex-example-to-match-multiline-string-in-rust)