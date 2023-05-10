# How to convert Rust bytes to hex?
// plain

To convert Rust bytes to hex, you can use the `format!` macro. This macro takes a format string and a list of arguments, and returns a `String` containing the formatted output. The format string `{:x}` will format the argument as a hexadecimal number.

```rust
let bytes = vec![0x41, 0x42, 0x43];
let hex_string = format!("{:x}", bytes);
println!("{}", hex_string);
```

## Output example

```
414243
```

The code above does the following:

1. Creates a vector of bytes (`vec![0x41, 0x42, 0x43]`)
2. Uses the `format!` macro to format the bytes as a hexadecimal number (`{:x}`)
3. Prints the resulting hexadecimal string (`414243`)

## Helpful links

- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)

group: rust-bytes