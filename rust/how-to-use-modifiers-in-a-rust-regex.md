# How to use modifiers in a Rust regex?
// plain

Modifiers are used to modify the behavior of a regular expression in Rust. They can be used to make a regex case-insensitive, to enable multi-line matching, and to enable Unicode support.

## Example code

```rust
let re = Regex::new(r"(?i)hello").unwrap();
```

## Output example

```
Regex
```

## Code explanation

- `Regex::new`: This is a function from the `regex` crate that creates a new Regex object.
- `r"(?i)hello"`: This is the regular expression that is passed to the `Regex::new` function. The `(?i)` modifier makes the regex case-insensitive.
- `unwrap`: This is a method on the `Result` type that is returned by the `Regex::new` function. It will either return the `Regex` object or panic if an error occurs.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Rust Regex Modifiers](https://doc.rust-lang.org/regex/regex/enum.Regex.html#method.set_flags)

group: rust-regex

onelinerhub: [How to use modifiers in a Rust regex?](https://onelinerhub.com/rust/how-to-use-modifiers-in-a-rust-regex)