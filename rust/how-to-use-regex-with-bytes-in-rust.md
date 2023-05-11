# How to use regex with bytes in Rust?
// plain

Regex can be used with bytes in Rust by using the `regex` crate. This crate provides a `Regex` type which can be used to match against byte slices.

```rust
use regex::Regex;

let re = Regex::new(r"\d+").unwrap();
let bytes = b"123 456";

for cap in re.captures_iter(bytes) {
    println!("{}", &cap[0]);
}
```

## Output example

```
123
456
```

## Code explanation

- `use regex::Regex`: imports the `Regex` type from the `regex` crate.
- `Regex::new(r"\d+")`: creates a new `Regex` object from the given pattern.
- `captures_iter(bytes)`: returns an iterator over all the non-overlapping captures in the given byte slice.
- `&cap[0]`: returns the first capture group of the given capture.

## Helpful links
- [Regex crate documentation](https://docs.rs/regex/1.3.9/regex/)
- [Regex tutorial](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to use regex with bytes in Rust?](https://onelinerhub.com/rust/how-to-use-regex-with-bytes-in-rust)