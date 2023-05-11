# How to use regex to match a group in Rust?
// plain

Regex (regular expressions) can be used to match a group in Rust. To do this, you need to use the `regex` crate.

## Example code

```rust
extern crate regex;
use regex::Regex;

fn main() {
    let re = Regex::new(r"(\w{5})").unwrap();
    let text = "The quick brown fox";
    for cap in re.captures_iter(text) {
        println!("{}", &cap[1]);
    }
}
```

## Output example

```
quick
brown
fox
```

## Code explanation

- `extern crate regex;`: imports the `regex` crate.
- `use regex::Regex;`: imports the `Regex` type from the `regex` crate.
- `let re = Regex::new(r"(\w{5})").unwrap();`: creates a new `Regex` object with the pattern `(\w{5})`.
- `let text = "The quick brown fox";`: creates a string to match against.
- `for cap in re.captures_iter(text) {`: iterates over the captures of the `Regex` object.
- `println!("{}", &cap[1]);`: prints the capture group.

## Helpful links
- [Regex crate documentation](https://docs.rs/regex/1.3.9/regex/)
- [Rust regex tutorial](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html)

group: rust-regex

onelinerhub: [How to use regex to match a group in Rust?](https://onelinerhub.com/rust/how-to-use-regex-to-match-a-group-in-rust)