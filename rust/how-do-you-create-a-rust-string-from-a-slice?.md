# How do you create a Rust string from a slice?
// plain

You can create a Rust string from a slice by using the `String::from` function. This function takes a `&str` slice and returns a `String` object.

## Example code

```
let slice = "Hello world!";
let string = String::from(slice);
```

## Output example

```
Hello world!
```

The code above creates a `String` object from a `&str` slice. The `&str` slice is passed as an argument to the `String::from` function, which returns a `String` object.

## Code explanation

- `let slice = "Hello world!";`: This creates a `&str` slice with the value "Hello world!".
- `let string = String::from(slice);`: This creates a `String` object from the `&str` slice.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/primitive.str.html)
- [Rust Documentation - String](https://doc.rust-lang.org/std/string/struct.String.html)