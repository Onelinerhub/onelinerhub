# How do I convert a string to bytes in Rust?
// plain

To convert a string to bytes in Rust, you can use the `as_bytes()` method. This method returns a `&[u8]` which is a slice of bytes.

## Example code

```
let my_string = "Hello World";
let my_bytes = my_string.as_bytes();
```

## Output example

```
[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
```

## Code explanation

- `let my_string = "Hello World";`: This declares a variable `my_string` and assigns it the value of the string `"Hello World"`.
- `let my_bytes = my_string.as_bytes();`: This calls the `as_bytes()` method on the `my_string` variable, and assigns the result to the `my_bytes` variable.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Slices](https://doc.rust-lang.org/std/primitive.slice.html)