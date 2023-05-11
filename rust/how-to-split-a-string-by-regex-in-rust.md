# How to split a string by regex in Rust?
// plain

Splitting a string by regex in Rust can be done using the `str::split` method. This method takes a `&str` and a `&str` representing a regular expression as arguments and returns an iterator over the substrings of the given string slice, separated by the regular expression.

## Example code

```rust
let s = "Hello, world!";
let re = r"\W+";

for part in s.split(re) {
    println!("{}", part);
}
```

## Output example

```
Hello
world
```

## Code explanation

- `let s = "Hello, world!";`: This line declares a `&str` variable `s` and assigns it the value `"Hello, world!"`.
- `let re = r"\W+";`: This line declares a `&str` variable `re` and assigns it the value `r"\W+"`, which is a regular expression representing one or more non-word characters.
- `for part in s.split(re)`: This line uses the `str::split` method to split the string `s` by the regular expression `re` and iterate over the resulting substrings.
- `println!("{}", part);`: This line prints each substring to the console.

## Helpful links
- [str::split](https://doc.rust-lang.org/std/primitive.str.html#method.split)

group: rust-regex

onelinerhub: [How to split a string by regex in Rust?](https://onelinerhub.com/rust/how-to-split-a-string-by-regex-in-rust)