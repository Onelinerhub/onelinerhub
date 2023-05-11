# How to find the first match in a Rust regex?
// plain

The `find` method of the `Regex` type can be used to find the first match in a Rust regex.

## Example code

```rust
let re = Regex::new(r"\d+").unwrap();
let text = "123 456 789";

let first_match = re.find(text).unwrap();
println!("{:?}", first_match);
```

## Output example

```
Some((0, 3))
```

## Code explanation


1. `let re = Regex::new(r"\d+").unwrap();`: This line creates a new `Regex` object from the given pattern. The `unwrap` method is used to handle any errors that may occur.

2. `let text = "123 456 789";`: This line creates a `String` object containing the text to be searched.

3. `let first_match = re.find(text).unwrap();`: This line calls the `find` method of the `Regex` object to find the first match in the given text. The `unwrap` method is used to handle any errors that may occur.

4. `println!("{:?}", first_match);`: This line prints the result of the `find` method.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)

group: rust-regex

onelinerhub: [How to find the first match in a Rust regex?](https://onelinerhub.com/rust/how-to-find-the-first-match-in-a-rust-regex)