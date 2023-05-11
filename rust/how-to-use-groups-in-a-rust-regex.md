# How to use groups in a Rust regex?
// plain

Groups in Rust regex are used to capture parts of a string that match a certain pattern. They are defined by enclosing the pattern in parentheses.

## Example

```
let re = Regex::new(r"(\w{5})").unwrap();
let text = "The quick brown fox";

for cap in re.captures_iter(text) {
    println!("{}", &cap[1]);
}
```
## Output example

```
quick
brown
```

## Code explanation

- `Regex::new(r"(\w{5})")`: creates a new Regex object with a pattern that matches any 5 word characters
- `captures_iter(text)`: iterates over the text and captures any matches of the pattern
- `&cap[1]`: prints the first capture group, which is the 5 word characters

## Helpful links
- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Regex Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)

group: rust-regex

onelinerhub: [How to use groups in a Rust regex?](https://onelinerhub.com/rust/how-to-use-groups-in-a-rust-regex)