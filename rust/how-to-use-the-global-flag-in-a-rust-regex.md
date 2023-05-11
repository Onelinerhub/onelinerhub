# How to use the global flag in a Rust regex?
// plain

The global flag in Rust regex is used to indicate that the pattern should be applied to all occurrences in the string. To use the global flag, the `g` flag should be added to the end of the regex pattern.

## Example code

```
let re = Regex::new(r"\d+").unwrap();
let text = "123 456 789";
let mut iter = re.captures_iter(text);

while let Some(cap) = iter.next() {
    println!("{}", &cap[0]);
}
```

## Output example

```
123
456
789
```

## Code explanation

- `let re = Regex::new(r"\d+").unwrap();`: This line creates a new Regex object with the pattern `\d+` which matches one or more digits.
- `let text = "123 456 789";`: This line creates a string with the text to be matched.
- `let mut iter = re.captures_iter(text);`: This line creates an iterator over the captures of the regex pattern in the text.
- `while let Some(cap) = iter.next() {`: This line starts a loop that will iterate over the captures of the regex pattern in the text.
- `println!("{}", &cap[0]);`: This line prints the capture of the regex pattern in the text.

## Helpful links
- [Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to use the global flag in a Rust regex?](https://onelinerhub.com/rust/how-to-use-the-global-flag-in-a-rust-regex)