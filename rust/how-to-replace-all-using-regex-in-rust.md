# How to replace all using regex in Rust?
// plain

Regex in Rust can be used to replace all occurrences of a pattern in a string. To do this, the `replace_all` method can be used.

```rust
let s = "Hello, world!";
let replaced = s.replace_all("world", "Rust");
println!("{}", replaced);
```

## Output example

```
Hello, Rust!
```

The `replace_all` method takes two parameters: a pattern and a replacement string. The pattern is a regular expression, and the replacement string is the string that will be used to replace all occurrences of the pattern.

## Code explanation

- `let s = "Hello, world!";`: This line declares a variable `s` and assigns it the value `"Hello, world!"`.
- `let replaced = s.replace_all("world", "Rust");`: This line calls the `replace_all` method on the `s` variable, passing in the pattern `"world"` and the replacement string `"Rust"`.
- `println!("{}", replaced);`: This line prints the value of the `replaced` variable, which is the result of the `replace_all` method.

## Helpful links
- [Rust Regex Documentation](https://docs.rs/regex/1.3.9/regex/)
- [Rust String Documentation](https://doc.rust-lang.org/std/string/struct.String.html)

group: rust-regex

onelinerhub: [How to replace all using regex in Rust?](https://onelinerhub.com/rust/how-to-replace-all-using-regex-in-rust)