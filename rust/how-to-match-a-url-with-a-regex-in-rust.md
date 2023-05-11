# How to match a URL with a regex in Rust?
// plain

Matching a URL with a regex in Rust is a simple process. The following example code block shows how to do this:
```rust
let re = Regex::new(r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$").unwrap();
let url = "https://www.example.com/path/to/page";

if re.is_match(url) {
    println!("URL matches the regex!");
}
```

The output of the example code is:
```
URL matches the regex!
```

## Code explanation

- `let re = Regex::new(r"^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$").unwrap();`: This line creates a new Regex object with the given regex pattern. The pattern matches URLs with the following format: `protocol://domain.tld/path/to/page`.
- `let url = "https://www.example.com/path/to/page";`: This line creates a string variable with the URL to be matched.
- `if re.is_match(url) {`: This line checks if the URL matches the regex pattern.
- `println!("URL matches the regex!");`: This line prints a message if the URL matches the regex pattern.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Rust Regex Tutorial](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html)

group: rust-regex

onelinerhub: [How to match a URL with a regex in Rust?](https://onelinerhub.com/rust/how-to-match-a-url-with-a-regex-in-rust)