# rust string build
// plain

A Rust `String` is a type of data structure used to store and manipulate text. It is a growable, mutable, owned, UTF-8 encoded string type. It is a heap-allocated data structure that is stored as a pointer.

```rust
let mut s = String::new();
s.push_str("Hello");
s.push(' ');
s.push_str("world!");

println!("{}", s);
```

## Output example

```
Hello world!
```

The code above creates a new `String` called `s` and then uses the `push_str()` and `push()` methods to add the text "Hello" and "world!" to it. Finally, it prints out the contents of the `String` using the `println!` macro.

The `String` type has many useful methods for manipulating text, such as `split()`, `replace()`, `trim()`, and `to_lowercase()`.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust by Example - Strings](https://doc.rust-lang.org/rust-by-example/std/str.html)