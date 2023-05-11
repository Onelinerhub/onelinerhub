# How to ignore case in Rust regex?
// plain

To ignore case in Rust regex, you can use the `i` flag. This flag will cause the regex to ignore case when matching. For example:

```rust
let re = Regex::new(r"(?i)hello").unwrap();
assert!(re.is_match("HELLO"));
```

The code above creates a regex with the `i` flag, which causes the regex to ignore case when matching. The `assert!` statement then checks that the regex matches the string `HELLO`, which it does.

The parts of the code are:

- `Regex::new(r"(?i)hello")`: This creates a new regex with the `i` flag, which causes the regex to ignore case when matching.
- `assert!(re.is_match("HELLO"))`: This checks that the regex matches the string `HELLO`, which it does.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to ignore case in Rust regex?](https://onelinerhub.com/rust/how-to-ignore-case-in-rust-regex)