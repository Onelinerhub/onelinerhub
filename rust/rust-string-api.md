# rust string api
// plain

Rust strings are a powerful and efficient way to store and manipulate text data. They are stored as UTF-8 encoded data, which allows for efficient storage and manipulation of text data. Rust strings are immutable, meaning that once created, they cannot be changed.

## Example code

```rust
let mut s = String::from("Hello");
s.push_str(", world!");
println!("{}", s);
```

## Output example

```
Hello, world!
```

## Code explanation

- `let mut s = String::from("Hello");`: This line creates a mutable string variable `s` and assigns it the value `Hello`.
- `s.push_str(", world!");`: This line adds the string `", world!"` to the end of the string `s`.
- `println!("{}", s);`: This line prints the value of the string `s` to the console.

## Helpful links
- [Rust Strings Documentation](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust String Tutorial](https://doc.rust-lang.org/book/ch08-02-strings.html)