# How to use Unicode in a regex in Rust?
// plain

Using Unicode in a regex in Rust is easy and straightforward. The `\p{<property>}` syntax can be used to match any character that has the specified Unicode property. For example, the following code block will match any character that is a letter:

```rust
let re = Regex::new(r"\p{L}").unwrap();
```

## Code explanation


- `Regex::new`: This is a static method of the `Regex` struct that creates a new `Regex` object from a given pattern.
- `r"\p{L}"`: This is the regex pattern that matches any character that is a letter. The `\p{<property>}` syntax is used to match any character that has the specified Unicode property.
- `unwrap`: This is a method of the `Result` type that returns the contained value of a `Result` if it is `Ok`, or panics if it is `Err`.

## Helpful links

- [Unicode Regular Expressions](https://doc.rust-lang.org/regex/regex/index.html#unicode-regular-expressions)
- [Regex Struct](https://doc.rust-lang.org/regex/regex/struct.Regex.html)
- [Result Enum](https://doc.rust-lang.org/std/result/enum.Result.html)

group: rust-regex

onelinerhub: [How to use Unicode in a regex in Rust?](https://onelinerhub.com/rust/how-to-use-unicode-in-a-regex-in-rust)