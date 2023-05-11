# How to match digits with regex in Rust?
// plain

Matching digits with regex in Rust can be done using the `\d` character class. This character class matches any single digit from 0 to 9.

## Example code

```rust
let re = Regex::new(r"\d").unwrap();
let text = "123";

for cap in re.captures_iter(text) {
    println!("{}", &cap[0]);
}
```

## Output example

```
1
2
3
```

## Code explanation

- `Regex::new(r"\d")`: creates a new Regex object with the pattern `\d` which matches any single digit from 0 to 9.
- `captures_iter(text)`: returns an iterator over all the captures in the text.
- `&cap[0]`: returns the first capture group, which in this case is the digit.

## Helpful links
- [Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Character Classes](https://doc.rust-lang.org/regex/regex/enum.Regex.html#character-classes)

group: rust-regex

onelinerhub: [How to match digits with regex in Rust?](https://onelinerhub.com/rust/how-to-match-digits-with-regex-in-rust)