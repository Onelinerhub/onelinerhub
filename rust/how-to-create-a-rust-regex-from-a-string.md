# How to create a Rust regex from a string?
// plain

Creating a Rust regex from a string is a simple process. The `Regex::new` function takes a string as an argument and returns a `Regex` object.

```rust
let re = Regex::new("[0-9]+").unwrap();
```

The `unwrap` method is used to convert the `Result` object returned by `Regex::new` into a `Regex` object.

## Code explanation


- `Regex::new`: This function takes a string as an argument and returns a `Regex` object.
- `unwrap`: This method is used to convert the `Result` object returned by `Regex::new` into a `Regex` object.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Rust Regex Tutorial](https://rust-lang-nursery.github.io/rust-cookbook/regex/matching.html)

group: rust-regex

onelinerhub: [How to create a Rust regex from a string?](https://onelinerhub.com/rust/how-to-create-a-rust-regex-from-a-string)