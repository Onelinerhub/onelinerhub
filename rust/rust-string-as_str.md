# rust string as_str
// plain

`as_str` is a method of the `String` type in the Rust programming language. It returns a string slice (`&str`) that contains the entire string. This method is useful when passing a `String` to a function that requires a `&str` argument.

## Example

```rust
let my_string = String::from("Hello world!");
let my_str = my_string.as_str();
println!("{}", my_str);
```
## Output example

```
Hello world!
```

## Code explanation

- `let my_string = String::from("Hello world!");`: This line creates a `String` from the string literal `"Hello world!"`.
- `let my_str = my_string.as_str();`: This line calls the `as_str` method on the `my_string` `String` to get a `&str` string slice.
- `println!("{}", my_str);`: This line prints the `my_str` string slice to the console.

## Helpful links
- [Rust String Documentation](https://doc.rust-lang.org/std/string/struct.String.html)