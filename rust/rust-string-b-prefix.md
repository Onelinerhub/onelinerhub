# rust string b prefix
// plain

A `String` in Rust is a UTF-8 encoded, growable piece of text. It can be created from a literal string or a `&str` reference. The `b` prefix is used to create a `&[u8]` byte slice from a string literal.

## Example

```
let byte_slice = b"Hello world!";
```

## Output example

```
[72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
```

The `b` prefix creates a byte slice from the string literal, which is a sequence of bytes. In this example, the byte slice contains the ASCII codes for each character in the string.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Documentation - Byte Strings](https://doc.rust-lang.org/book/ch08-03-string-slices.html#byte-strings)