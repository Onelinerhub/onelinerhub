# How to extract data with regex in Rust?
// plain

Regex (regular expressions) can be used to extract data from strings in Rust. To use regex, the `regex` crate must be imported.

```rust
extern crate regex;

use regex::Regex;

fn main() {
    let re = Regex::new(r"\d+").unwrap();
    let text = "The answer is 42";

    println!("{:?}", re.find(text));
}
```

## Output example

```
Some("42")
```

The code above uses the `Regex::new` function to create a new Regex object from a string. The `find` method is then used to search for the first occurrence of the regex pattern in the given string.

Parts of the code:
- `extern crate regex`: imports the `regex` crate.
- `use regex::Regex`: imports the `Regex` type from the `regex` crate.
- `Regex::new(r"\d+")`: creates a new Regex object from the given string.
- `find(text)`: searches for the first occurrence of the regex pattern in the given string.

## Helpful links
- [Rust Regex Documentation](https://docs.rs/regex/1.3.9/regex/)
- [Rust Regex Tutorial](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html)

group: rust-regex

onelinerhub: [How to extract data with regex in Rust?](https://onelinerhub.com/rust/how-to-extract-data-with-regex-in-rust)