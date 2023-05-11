# How to convert a Rust slice to a string?
// plain

To convert a Rust slice to a String, you can use the `String::from_utf8` method. This method takes a `&[u8]` slice and returns a `Result<String, FromUtf8Error>`.

## Example code

```rust
let slice = [104, 101, 108, 108, 111];
let string = String::from_utf8(slice).unwrap();
println!("{}", string);
```

## Output example

```
hello
```

## Code explanation

- `let slice = [104, 101, 108, 108, 111];`: This creates a `&[u8]` slice containing the ASCII values for the characters `h`, `e`, `l`, `l`, and `o`.
- `let string = String::from_utf8(slice).unwrap();`: This calls the `String::from_utf8` method on the `slice` variable, which returns a `Result<String, FromUtf8Error>`. The `unwrap` method is used to get the `String` from the `Result`.
- `println!("{}", string);`: This prints the `String` to the console.

## Helpful links
- [String::from_utf8](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8)
- [FromUtf8Error](https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html)

group: rust-slice