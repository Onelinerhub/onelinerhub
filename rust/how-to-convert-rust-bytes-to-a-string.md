# How to convert Rust bytes to a string?
// plain

To convert Rust bytes to a string, you can use the `str::from_utf8` function. This function takes a `&[u8]` as an argument and returns a `Result<&str, Utf8Error>`.

## Example code

```rust
let bytes = b"Hello world!";
let string = str::from_utf8(bytes).unwrap();
println!("{}", string);
```

## Output example

```
Hello world!
```

## Code explanation

- `let bytes = b"Hello world!";`: This line creates a byte array containing the string "Hello world!".
- `let string = str::from_utf8(bytes).unwrap();`: This line calls the `str::from_utf8` function with the byte array as an argument. The `unwrap` method is used to get the `&str` from the `Result<&str, Utf8Error>` returned by the function.
- `println!("{}", string);`: This line prints the string to the console.

## Helpful links
- [str::from_utf8](https://doc.rust-lang.org/std/str/fn.from_utf8.html)

group: rust-bytes