# How to use named capture groups in Rust regex?
// plain

Named capture groups in Rust regex are used to capture a part of a string and assign it a name. This allows for easier access to the captured part of the string.

## Example code

```rust
let re = Regex::new(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})").unwrap();
let caps = re.captures("2020-04-30").unwrap();
println!("Year: {}", caps.name("year").unwrap());
println!("Month: {}", caps.name("month").unwrap());
println!("Day: {}", caps.name("day").unwrap());
```

## Output example

```
Year: 2020
Month: 04
Day: 30
```

## Code explanation

- `let re = Regex::new(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})").unwrap();`: This line creates a new Regex object with the pattern `(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})`. The `?P<year>` and `?P<month>` and `?P<day>` are the named capture groups.
- `let caps = re.captures("2020-04-30").unwrap();`: This line captures the string `2020-04-30` using the Regex object `re`.
- `println!("Year: {}", caps.name("year").unwrap());`: This line prints the value of the capture group `year` which is `2020`.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Named Capture Groups in Rust Regex](https://doc.rust-lang.org/regex/regex/struct.Regex.html#method.captures_named)

group: rust-regex

onelinerhub: [How to use named capture groups in Rust regex?](https://onelinerhub.com/rust/how-to-use-named-capture-groups-in-rust-regex)