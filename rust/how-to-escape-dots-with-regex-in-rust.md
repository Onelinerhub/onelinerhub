# How to escape dots with regex in Rust?
// plain

Regex in Rust can be used to escape dots with the `\` character. The `\` character is used to escape special characters in regex. For example, the following code block:

```rust
let re = Regex::new(r"\.\d+").unwrap();
```

will create a regex that matches strings containing a dot followed by one or more digits. The `\` character is used to escape the dot so that it is treated as a literal character instead of a special character.

The following code block shows how to use the regex to match a string containing a dot:

```rust
let text = "This is a string with a .5 in it";
let captures = re.captures(text).unwrap();
assert_eq!(captures[0], ".5");
```

The code above will match the string `.5` in the text and store it in the `captures` variable.

## Code explanation


- `Regex::new`: This is a function used to create a new regex object.
- `r"\.\d+"`: This is the regex pattern used to match a dot followed by one or more digits. The `\` character is used to escape the dot.
- `captures`: This is a function used to match the regex pattern against a string and return the matched string.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to escape dots with regex in Rust?](https://onelinerhub.com/rust/how-to-escape-dots-with-regex-in-rust)