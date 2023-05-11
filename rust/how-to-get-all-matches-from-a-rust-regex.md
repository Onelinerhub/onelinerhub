# How to get all matches from a Rust regex?
// plain

To get all matches from a Rust regex, you can use the `find_iter` method on a `Regex` object. This method returns an iterator of `Match` objects, which can be used to access the matched text.

## Example code

```rust
let re = Regex::new(r"\d+").unwrap();
let text = "123 456 789";

for m in re.find_iter(text) {
    println!("{}", m.as_str());
}
```

## Output example

```
123
456
789
```

## Code explanation

- `Regex::new(r"\d+")`: creates a new `Regex` object from the given regular expression.
- `find_iter(text)`: returns an iterator of `Match` objects from the given text.
- `m.as_str()`: returns the matched text as a string.

## Helpful links
- [Regex documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [`find_iter` documentation](https://doc.rust-lang.org/regex/regex/struct.Regex.html#method.find_iter)

group: rust-regex

onelinerhub: [How to get all matches from a Rust regex?](https://onelinerhub.com/rust/how-to-get-all-matches-from-a-rust-regex)