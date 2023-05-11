# How to replace a capture group using Rust regex?
// plain

Replacing a capture group using Rust regex is a simple process. The `replace_all` method of the `Regex` type can be used to replace a capture group with a given string.

## Example code

```rust
let re = Regex::new(r"(\d+)").unwrap();
let result = re.replace_all("My number is 123", "456");
```

## Output example

```
My number is 456
```

The code above creates a new `Regex` object with the pattern `(\d+)` which captures any sequence of digits. The `replace_all` method is then used to replace the captured group with the string `456`.

## Code explanation


1. `let re = Regex::new(r"(\d+)").unwrap();` - creates a new `Regex` object with the pattern `(\d+)` which captures any sequence of digits.
2. `let result = re.replace_all("My number is 123", "456");` - uses the `replace_all` method to replace the captured group with the string `456`.

## Helpful links

- [Rust Regex Documentation](https://docs.rs/regex/1.3.9/regex/)

group: rust-regex

onelinerhub: [How to replace a capture group using Rust regex?](https://onelinerhub.com/rust/how-to-replace-a-capture-group-using-rust-regex)