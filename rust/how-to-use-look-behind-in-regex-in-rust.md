# How to use look behind in regex in Rust?
// plain

Look behind is a feature of regular expressions that allows you to match a pattern only if it is preceded by another pattern. In Rust, look behind is supported by the `regex` crate.

## Example code

```rust
use regex::Regex;

let re = Regex::new(r"(?<=foo)bar").unwrap();
let text = "foobar";

assert!(re.is_match(text));
```

## Output example

```
true
```

## Code explanation

- `use regex::Regex`: imports the `Regex` type from the `regex` crate.
- `let re = Regex::new(r"(?<=foo)bar").unwrap()`: creates a new `Regex` object from the given pattern. The `?<=` syntax is used to specify a look behind pattern.
- `let text = "foobar"`: creates a string to match against.
- `assert!(re.is_match(text))`: checks if the given string matches the regular expression.

## Helpful links
- [Regex crate documentation](https://docs.rs/regex/1.3.9/regex/)
- [Look behind in Rust](https://doc.rust-lang.org/regex/regex/index.html#look-behind-assertions)

group: rust-regex

onelinerhub: [How to use look behind in regex in Rust?](https://onelinerhub.com/rust/how-to-use-look-behind-in-regex-in-rust)