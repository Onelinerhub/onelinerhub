# How to concat strings in Rust
// plain

Strings in Rust can be concatenated using the `+` operator. The following ## Code example shows how to concatenate two strings:

```
let s1 = "Hello";
let s2 = "World";
let s3 = s1 + " " + s2;
println!("{}", s3);
```

### Output

`Hello World`

The code above does the following:

1. Declares two strings `s1` and `s2` with the values `Hello` and `World` respectively.
2. Concatenates the two strings using the `+` operator and assigns the result to `s3`.
3. Prints the value of `s3` to the console.

For more information on string concatenation in Rust, please refer to the following links:

- [Rust Documentation - Strings](https://doc.rust-lang.org/stable/std/string/index.html)
- [Rust by Example - Strings](https://doc.rust-lang.org/stable/rust-by-example/std/str.html)