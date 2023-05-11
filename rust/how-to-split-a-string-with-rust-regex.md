# How to split a string with Rust regex?
// plain

Rust regex can be used to split a string into multiple parts. The `split` method of the `Regex` type can be used to split a string. The following example code splits a string into words using a space as the delimiter:
```rust
let re = Regex::new(r"\s+").unwrap();
let words = re.split("This is a string").collect::<Vec<&str>>();
```
The output of the above code is:
```
["This", "is", "a", "string"]
```

The code consists of the following parts:

1. `let re = Regex::new(r"\s+").unwrap();` - This line creates a new `Regex` object using the `Regex::new` method. The `\s+` is a regular expression that matches one or more whitespace characters. The `unwrap` method is used to convert the `Result` type returned by the `Regex::new` method into a `Regex` type.

2. `let words = re.split("This is a string").collect::<Vec<&str>>();` - This line uses the `split` method of the `Regex` type to split the string into words. The `collect` method is used to convert the iterator returned by the `split` method into a `Vec<&str>` type.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Rust Regex Tutorial](https://rust-lang-nursery.github.io/rust-cookbook/regex/matching.html)

group: rust-regex

onelinerhub: [How to split a string with Rust regex?](https://onelinerhub.com/rust/how-to-split-a-string-with-rust-regex)