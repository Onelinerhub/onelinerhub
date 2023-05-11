# How to use non-capturing groups in Rust regex?
// plain

Non-capturing groups in Rust regex are used to group multiple regular expressions together without capturing the result of the group. They are denoted by `(?: )` and can be used to apply quantifiers to multiple expressions at once.

## Example code

```
let re = Regex::new(r"(?:a|b)*").unwrap();
assert!(re.is_match("ababab"));
```

## Output example

```
true
```

## Code explanation

- `Regex::new(r"(?:a|b)*")`: creates a new Regex object with a non-capturing group containing two regular expressions, `a` and `b`.
- `unwrap()`: unwraps the Regex object from the Result type.
- `is_match("ababab")`: checks if the given string matches the regular expression.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Non-capturing Groups in Regex](https://www.regular-expressions.info/brackets.html)

group: rust-regex

onelinerhub: [How to use non-capturing groups in Rust regex?](https://onelinerhub.com/rust/how-to-use-non-capturing-groups-in-rust-regex)