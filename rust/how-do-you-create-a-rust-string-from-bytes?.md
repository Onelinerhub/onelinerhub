# How do you create a Rust string from bytes?
// plain

You can create a Rust string from bytes using the `String::from_utf8()` method. This method takes a `&[u8]` as an argument and returns a `Result<String, FromUtf8Error>`.

## Example code

```rust
let bytes = [104, 101, 108, 108, 111];
let string = String::from_utf8(bytes).unwrap();
```

## Output example

```
hello
```

The code above creates a `String` from the given bytes. The `String::from_utf8()` method takes a `&[u8]` as an argument and returns a `Result<String, FromUtf8Error>`. The `unwrap()` method is used to get the `String` from the `Result`.

## Helpful links

- [String::from_utf8()](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8)
- [Result](https://doc.rust-lang.org/std/result/enum.Result.html)
- [unwrap()](https://doc.rust-lang.org/std/result/enum.Result.html#method.unwrap)