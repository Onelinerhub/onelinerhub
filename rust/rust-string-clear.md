# rust string clear
// plain

Rust strings are a type of data structure used to store and manipulate text. They are stored as a sequence of Unicode scalar values, which are encoded as a sequence of bytes.

```
let mut s = String::new();
s.clear();
```

The `clear()` method is used to clear a string, setting it to an empty string. This method does not take any arguments and does not return any value.

- `let mut s = String::new()`: creates a new, empty string
- `s.clear()`: clears the string, setting it to an empty string

## Helpful links
- [Rust Strings Documentation](https://doc.rust-lang.org/std/string/struct.String.html)