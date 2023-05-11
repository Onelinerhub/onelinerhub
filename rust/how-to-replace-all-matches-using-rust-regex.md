# How to replace all matches using Rust regex?
// plain

Regex in Rust can be used to replace all matches with the `replace_all` method. This method takes a string and a closure as parameters. The closure is used to determine what the replacement string should be.

## Example code

```
let re = Regex::new(r"(\w+)").unwrap();
let text = "Hello world";
let result = re.replace_all(text, |caps: &Captures| {
    let word = &caps[1];
    format!("{}!", word)
});
```

## Output example

```
Hello! world!
```

## Code explanation

- `Regex::new(r"(\w+)")`: creates a new Regex object with the given pattern.
- `replace_all(text, |caps: &Captures| {...})`: replaces all matches of the Regex object with the given closure. The closure takes a `Captures` object as parameter, which contains the matched strings.
- `&caps[1]`: gets the first matched string from the `Captures` object.
- `format!("{}!", word)`: creates a new string with the given format.

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to replace all matches using Rust regex?](https://onelinerhub.com/rust/how-to-replace-all-matches-using-rust-regex)