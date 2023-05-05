# rust string concat
// plain

Rust strings can be concatenated using the `+` operator. For example:

```rust
let s1 = "Hello";
let s2 = "World";
let s3 = s1 + " " + s2;
```

The output of the above code is:

```
Hello World
```

The `+` operator can be used to concatenate two strings, or a string and a string literal. The `format!` macro can also be used to concatenate strings, and it allows for more complex string formatting.

## Code explanation


- `let s1 = "Hello";`: This line declares a string variable `s1` and assigns it the value `"Hello"`.
- `let s2 = "World";`: This line declares a string variable `s2` and assigns it the value `"World"`.
- `let s3 = s1 + " " + s2;`: This line concatenates the strings `s1` and `s2` with a space in between, and assigns the result to the variable `s3`.
- `format!` macro: This macro allows for more complex string formatting and concatenation.

## Helpful links

- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Format Macro](https://doc.rust-lang.org/std/macro.format.html)