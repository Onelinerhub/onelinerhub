# How to count number of lines in a string in Rust?
// plain

To count the number of lines in a string in Rust, you can use the `lines()` method of the `str` type. This method returns an iterator over the lines of the string. The following example code block shows how to use the `lines()` method to count the number of lines in a string:

```rust
let s = "This is a string
with multiple lines";

let line_count = s.lines().count();

println!("The string has {} lines", line_count);
```

The output of the example code is:

```
The string has 2 lines
```

The code works as follows:

1. The `let s = ...` line creates a string variable `s` with the value `This is a string\nwith multiple lines`.
2. The `let line_count = s.lines().count()` line calls the `lines()` method on the `s` string, which returns an iterator over the lines of the string. The `count()` method is then called on the iterator, which returns the number of lines in the string.
3. The `println!("The string has {} lines", line_count)` line prints the number of lines in the string to the console.

## Helpful links

- [Rust Str Type Documentation](https://doc.rust-lang.org/std/primitive.str.html)