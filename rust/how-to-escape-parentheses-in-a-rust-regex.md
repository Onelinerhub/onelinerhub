# How to escape parentheses in a Rust regex?
// plain

To escape parentheses in a Rust regex, you can use a backslash (`\`) before the parentheses. For example:

```
let re = Regex::new(r"\(test\)").unwrap();
```

This will create a regex that matches the literal string `(test)`.

## Code explanation


- `let re =`: This declares a variable `re` of type `Regex`.
- `Regex::new`: This is a static method of the `Regex` type that creates a new `Regex` from a string.
- `r"\(test\)"`: This is the string passed to `Regex::new`. The `r` indicates that it is a raw string, which means that backslashes are not treated as escape characters. The backslash before the parentheses escapes them, so that the regex matches the literal string `(test)`.

## Helpful links

- [The Rust Programming Language - Regular Expressions](https://doc.rust-lang.org/book/ch19-05-advanced-regular-expressions.html)

group: rust-regex

onelinerhub: [How to escape parentheses in a Rust regex?](https://onelinerhub.com/rust/how-to-escape-parentheses-in-a-rust-regex)