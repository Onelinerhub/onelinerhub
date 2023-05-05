# What encoding is used for Rust strings?
// plain

Rust strings are encoded using UTF-8. UTF-8 is a variable-width encoding that can represent every character in the Unicode character set. It is the most popular encoding used for web pages and other documents on the internet.

## Example code

```
let s = "Hello, world!";
println!("{}", s);
```

## Output example

```
Hello, world!
```

## Code explanation

- `let s = "Hello, world!";`: This line declares a variable `s` and assigns it the string value `"Hello, world!"`.
- `println!("{}", s);`: This line prints the value of the variable `s` to the console.

## Helpful links
- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)