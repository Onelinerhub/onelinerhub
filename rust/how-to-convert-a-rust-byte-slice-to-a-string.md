# How to convert a Rust byte slice to a string?
// plain

To convert a Rust byte slice to a string, you can use the `std::str::from_utf8` function. This function takes a byte slice and returns a `Result<&str, Utf8Error>`.

## Example code

```rust
let bytes = b"Hello world!";
let string = std::str::from_utf8(bytes).unwrap();
```

## Output example

```
Hello world!
```

## Code explanation

- `let bytes = b"Hello world!";`: This creates a byte slice containing the bytes of the string "Hello world!".
- `let string = std::str::from_utf8(bytes).unwrap();`: This calls the `std::str::from_utf8` function, passing in the byte slice `bytes`. The `unwrap` method is used to get the `&str` from the `Result` returned by the function.

## Helpful links
- [std::str::from_utf8](https://doc.rust-lang.org/std/str/fn.from_utf8.html)

group: rust-slice