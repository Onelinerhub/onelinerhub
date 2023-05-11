# How to use negation in Rust regex?
// plain

Negation in Rust regex can be used to match any character except the one specified. To use negation, the `^` character is used inside a character set `[]`.

For example, the following code will match any character except `a`:
```
let re = Regex::new(r"[^a]").unwrap();
assert!(re.is_match("b"));
```

The code consists of the following parts:
1. `Regex::new(r"[^a]")` - creates a new Regex object with the pattern `[^a]`, which matches any character except `a`
2. `unwrap()` - unwraps the Result object returned by `Regex::new()`
3. `assert!(re.is_match("b"))` - checks if the Regex object `re` matches the string `b`

For more information, see the [Rust Regex documentation](https://doc.rust-lang.org/regex/regex/index.html).

group: rust-regex

onelinerhub: [How to use negation in Rust regex?](https://onelinerhub.com/rust/how-to-use-negation-in-rust-regex)