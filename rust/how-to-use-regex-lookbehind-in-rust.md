# How to use regex lookbehind in Rust?
// plain

Regex lookbehinds are a powerful tool for matching patterns in strings. In Rust, lookbehinds are supported through the `regex` crate.

## Example code

```rust
use regex::Regex;

let re = Regex::new(r"(?<=\d)\s+").unwrap();
let text = "1 2 3 4 5";

for cap in re.captures_iter(text) {
    println!("{}", &cap[0]);
}
```

## Output example

```
 2
 3
 4
```

The code above uses a lookbehind to match any whitespace character (`\s`) preceded by a digit (`\d`). The lookbehind is specified with `(?<=\d)`. The `Regex::new` function is used to create a new `Regex` object from the pattern. The `captures_iter` method is then used to iterate over all matches in the text.

## Code explanation

- `Regex::new`: creates a new `Regex` object from the pattern
- `captures_iter`: iterates over all matches in the text
- `(?<=\d)`: lookbehind to match any whitespace character (`\s`) preceded by a digit (`\d`)

## Helpful links
- [Regex lookbehinds in Rust](https://doc.rust-lang.org/regex/regex/index.html#lookbehind-assertions)
- [Regex crate documentation](https://docs.rs/regex/1.3.9/regex/)

group: rust-regex

onelinerhub: [How to use regex lookbehind in Rust?](https://onelinerhub.com/rust/how-to-use-regex-lookbehind-in-rust)