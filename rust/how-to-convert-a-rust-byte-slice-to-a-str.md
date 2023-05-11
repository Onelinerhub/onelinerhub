# How to convert a Rust byte slice to a str?
// plain

To convert a Rust byte slice to a str, you can use the `str::from_utf8` function. This function takes a byte slice and returns a `Result<&str, Utf8Error>`.

## Example code

```rust
let bytes = b"Hello world!";
let s = str::from_utf8(bytes).unwrap();
println!("{}", s);
```

## Output example

```
Hello world!
```

## Code explanation

- `let bytes = b"Hello world!";`: This creates a byte slice containing the string "Hello world!".
- `let s = str::from_utf8(bytes).unwrap();`: This calls the `str::from_utf8` function, passing in the byte slice `bytes`. The `unwrap` method is used to get the `&str` from the `Result` returned by the function.
- `println!("{}", s);`: This prints the `&str` to the console.

## Helpful links
- [str::from_utf8](https://doc.rust-lang.org/std/str/fn.from_utf8.html)

group: rust-slice