# How to use regex lookahead in Rust?
// plain

Regex lookahead is a powerful tool for pattern matching in Rust. It allows you to match patterns that are not necessarily adjacent to each other.

## Example code

```
let re = Regex::new(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}").unwrap();
let text = "MyPassword123";
assert!(re.is_match(text));
```

## Output example

```
true
```

## Code explanation

- `Regex::new`: creates a new Regex object from a given pattern string
- `(?=.*\d)`: lookahead assertion that checks for at least one digit
- `(?=.*[a-z])`: lookahead assertion that checks for at least one lowercase letter
- `(?=.*[A-Z])`: lookahead assertion that checks for at least one uppercase letter
- `.{8,}`: checks for at least 8 characters
- `is_match`: checks if the given text matches the pattern

## Helpful links
- [Regex Lookahead Assertions](https://doc.rust-lang.org/regex/regex/index.html#lookahead-assertions)
- [Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to use regex lookahead in Rust?](https://onelinerhub.com/rust/how-to-use-regex-lookahead-in-rust)