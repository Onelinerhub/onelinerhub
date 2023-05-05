# rust string and str
// plain

A `String` in Rust is a type of data structure that stores a collection of characters. It is a heap-allocated data structure and is growable, meaning it can be appended to. `str` is a type of string literal that is statically allocated and is not growable.

## Example code

```rust
let mut s = String::from("Hello");
s.push_str(", world!");

let s2 = "Hello, world!";
```

## Output example

```
Hello, world!
```

## Code explanation

- `let mut s = String::from("Hello");`: This line creates a mutable `String` called `s` and assigns it the value `"Hello"`.
- `s.push_str(", world!");`: This line appends the string `", world!"` to the end of `s`.
- `let s2 = "Hello, world!";`: This line creates a `str` called `s2` and assigns it the value `"Hello, world!"`.

## Helpful links
- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust String vs &str](https://stackoverflow.com/questions/44013571/what-is-the-difference-between-string-and-str-in-rust)