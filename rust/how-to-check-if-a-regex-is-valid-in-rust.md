# How to check if a regex is valid in Rust?
// plain

To check if a regex is valid in Rust, you can use the `is_match` method from the `regex` crate. This method takes a string and a regular expression as parameters and returns a boolean value indicating whether the string matches the regular expression.

## Example code

```rust
use regex::Regex;

let re = Regex::new(r"^\d{4}-\d{2}-\d{2}$").unwrap();
let is_valid = re.is_match("2020-01-01");

println!("{}", is_valid);
```

## Output example

```
true
```

## Code explanation

- `use regex::Regex;`: imports the `Regex` type from the `regex` crate.
- `let re = Regex::new(r"^\d{4}-\d{2}-\d{2}$").unwrap();`: creates a new `Regex` object from the given regular expression. The `unwrap` method is used to convert the `Result` type returned by `Regex::new` into a `Regex` object.
- `let is_valid = re.is_match("2020-01-01");`: calls the `is_match` method on the `Regex` object, passing in a string to check against the regular expression.
- `println!("{}", is_valid);`: prints the boolean value returned by `is_match`.

## Helpful links
- [Regex documentation](https://docs.rs/regex/1.3.9/regex/)

group: rust-regex

onelinerhub: [How to check if a regex is valid in Rust?](https://onelinerhub.com/rust/how-to-check-if-a-regex-is-valid-in-rust)