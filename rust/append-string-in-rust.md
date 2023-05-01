# Append string in Rust
// plain

String concatenation in Rust can be done using the `+` operator or the `format!` macro.

## Code example:

```
let mut s = String::from("Hello");
s.push_str(", world!");
println!("{}", s);
```

### Output

`Hello, world!`

## Explanation of code parts:

1. `let mut s = String::from("Hello");` - This line creates a mutable `String` variable `s` and assigns it the value `Hello`.
2. `s.push_str(", world!");` - This line appends the string `", world!"` to the existing string `s`.
3. `println!("{}", s);` - This line prints the value of `s` to the console.

## Helpful links:

1. [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
2. [Rust by Example - Strings](https://doc.rust-lang.org/rust-by-example/strings.html)
