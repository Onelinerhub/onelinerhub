# How to use regex captures in Rust?
// plain

Regex captures in Rust are used to capture substrings from a given string. Captures are stored in a `Vec` and can be accessed by index.

## Example code

```rust
let re = Regex::new(r"(\d{4})-(\d{2})-(\d{2})").unwrap();
let text = "Today is 2020-07-30";
let captures = re.captures(text).unwrap();
println!("Year: {}", &captures[1]);
println!("Month: {}", &captures[2]);
println!("Day: {}", &captures[3]);
```

## Output example

```
Year: 2020
Month: 07
Day: 30
```

## Code explanation

- `let re = Regex::new(r"(\d{4})-(\d{2})-(\d{2})").unwrap();`: This line creates a new `Regex` object with the given pattern. The pattern `(\d{4})-(\d{2})-(\d{2})` matches a date in the format `YYYY-MM-DD`.
- `let text = "Today is 2020-07-30";`: This line creates a string with the date to be matched.
- `let captures = re.captures(text).unwrap();`: This line captures the substrings from the given string using the `Regex` object.
- `println!("Year: {}", &captures[1]);`: This line prints the first capture, which is the year.
- `println!("Month: {}", &captures[2]);`: This line prints the second capture, which is the month.
- `println!("Day: {}", &captures[3]);`: This line prints the third capture, which is the day.

## Helpful links
- [Regex Captures in Rust](https://doc.rust-lang.org/regex/regex/struct.Captures.html)
- [Regex in Rust](https://doc.rust-lang.org/regex/index.html)

group: rust-regex

onelinerhub: [How to use regex captures in Rust?](https://onelinerhub.com/rust/how-to-use-regex-captures-in-rust)