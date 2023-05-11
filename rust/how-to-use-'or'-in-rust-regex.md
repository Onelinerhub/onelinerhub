# How to use 'or' in Rust regex?
// plain

The `or` operator in Rust regex is used to match one of several possible patterns. It is written as `|` and can be used to match multiple patterns in a single expression.

For example, the following code will match either `foo` or `bar`:
```
let re = regex!(r"foo|bar");
```

## Code explanation

- `|`: The `or` operator
- `regex!`: A macro used to create a Regex object
- `r"foo|bar"`: The regex pattern, which matches either `foo` or `bar`

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to use 'or' in Rust regex?](https://onelinerhub.com/rust/how-to-use-%27or%27-in-rust-regex)