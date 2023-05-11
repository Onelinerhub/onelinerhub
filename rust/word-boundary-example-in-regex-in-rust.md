# Word boundary example in regex in Rust
// plain

Word boundary in regex is a zero-width assertion that matches the position between a word character (a-z, A-Z, 0-9, and _) and a non-word character. In Rust, it is represented by the `\b` character.

## Example code

```
let re = Regex::new(r"\bword\b").unwrap();
let text = "This is a word";

println!("{}", re.is_match(text));
```

## Output example

```
true
```

## Code explanation

- `Regex::new(r"\bword\b")`: creates a new Regex object with the pattern `\bword\b`
- `let text = "This is a word"`: creates a string variable with the text `This is a word`
- `re.is_match(text)`: checks if the Regex pattern matches the text

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Word Boundary in Regex](https://www.regular-expressions.info/wordboundaries.html)

group: rust-regex

onelinerhub: [Word boundary example in regex in Rust](https://onelinerhub.com/rust/word-boundary-example-in-regex-in-rust)