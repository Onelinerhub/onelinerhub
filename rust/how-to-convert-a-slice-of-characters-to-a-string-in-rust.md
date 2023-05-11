# How to convert a slice of characters to a string in Rust?
// plain

To convert a slice of characters to a string in Rust, you can use the `String::from` function. This function takes a `&str` as an argument and returns a `String` type.

## Example code

```
let chars = ['h', 'e', 'l', 'l', 'o'];
let string = String::from(&chars[..]);
```

## Output example

```
hello
```

The code above creates a slice of characters `chars` and then uses the `String::from` function to convert it to a `String` type. The `&` before the `chars` indicates that the function takes a reference to the slice.

## Code explanation

- `let chars = ['h', 'e', 'l', 'l', 'o'];`: This creates a slice of characters.
- `let string = String::from(&chars[..]);`: This uses the `String::from` function to convert the slice of characters to a `String` type. The `&` before the `chars` indicates that the function takes a reference to the slice.

## Helpful links
- [String::from](https://doc.rust-lang.org/std/string/struct.String.html#method.from)

group: rust-slice