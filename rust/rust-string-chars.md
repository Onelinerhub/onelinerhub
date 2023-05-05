# rust string chars
// plain

A `String` in Rust is a UTF-8 encoded sequence of bytes. It is a collection of characters, and each character is represented by a `char` type.

```rust
let s = String::from("Hello, world!");

for c in s.chars() {
    println!("{}", c);
}
```

The output of the above code is:
```
H
e
l
l
o
,

w
o
r
l
d
!
```

The `chars()` method of a `String` returns an iterator over the characters of the string. This iterator can be used to iterate over the characters of the string.

The `char` type in Rust is a Unicode scalar value, which means it can represent a code point in any Unicode code point range.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Chars](https://doc.rust-lang.org/std/primitive.char.html)