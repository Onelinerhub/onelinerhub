# rust string append
// plain

Rust strings are immutable, meaning that once created, they cannot be changed. However, it is possible to append a string to an existing string using the `push_str()` method.

## Example code

```
let mut s = String::from("Hello");
s.push_str(", world!");
```

## Output example

```
Hello, world!
```

The code above creates a `String` object called `s` and assigns it the value `Hello`. The `push_str()` method is then used to append the string `, world!` to the existing string. The result is a new string with the value `Hello, world!`.

The `push_str()` method takes a `&str` as an argument, so it is possible to append a string literal or a string slice to an existing string.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust by Example - Strings](https://doc.rust-lang.org/rust-by-example/std/str.html)