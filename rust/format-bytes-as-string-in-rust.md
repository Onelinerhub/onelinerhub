# Format bytes as string in Rust
// plain

You can format bytes as a string in Rust using the [`format_args!`](https://doc.rust-lang.org/std/macro.format_args.html) macro. This macro takes a format string and a list of arguments and returns a formatted string.

Example:

```
let bytes = 1024;
let formatted_string = format_args!("{} bytes", bytes);
println!("{}", formatted_string);
```

### Output

```
1024 bytes
```

Explanation:

1. The `let bytes = 1024;` line declares a variable `bytes` and assigns it the value `1024`.
2. The `let formatted_string = format_args!("{} bytes", bytes);` line uses the `format_args!` macro to format the `bytes` variable as a string with the format `{} bytes`.
3. The `println!("{}", formatted_string);` line prints the formatted string to the console.