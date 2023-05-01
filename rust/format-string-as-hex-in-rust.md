# Format string as hex in Rust
// plain

Formatting a string as hex in Rust can be done using the `format!` macro. The `format!` macro takes a format string and a list of arguments and returns a `String` object. The format string can contain special formatting characters that will be replaced with the corresponding argument. To format a string as hex, the `{:x}` formatting character can be used.

## Code example:
```
let my_string = "Hello World";
let hex_string = format!("{:x}", my_string);
println!("{}", hex_string);
```

### Output
`48656c6c6f20576f726c64`

Explanation:
- `let my_string = "Hello World";`: This line declares a variable `my_string` and assigns it the value `"Hello World"`.
- `let hex_string = format!("{:x}", my_string);`: This line uses the `format!` macro to format `my_string` as hex and assigns the result to the variable `hex_string`. The `{:x}` formatting character tells the `format!` macro to format the argument as hex.
- `println!("{}", hex_string);`: This line prints the value of `hex_string` to the console.

## Helpful links:
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust Documentation - Primitive Formatting](https://doc.rust-lang.org/std/fmt/index.html#primitive-formatting)