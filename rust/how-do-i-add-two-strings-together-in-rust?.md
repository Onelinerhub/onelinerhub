# How do I add two strings together in Rust?
// plain

Adding two strings together in Rust is a simple process. The `+` operator is used to concatenate two strings. For example:

```
let s1 = "Hello";
let s2 = "World";
let s3 = s1 + " " + s2;
println!("{}", s3);
```

This code will output `Hello World`.

## Code explanation


- `let s1 = "Hello";` - This declares a string variable `s1` and assigns it the value `Hello`.
- `let s2 = "World";` - This declares a string variable `s2` and assigns it the value `World`.
- `let s3 = s1 + " " + s2;` - This declares a string variable `s3` and assigns it the value of `s1` concatenated with a space and `s2`.
- `println!("{}", s3);` - This prints the value of `s3` to the console.

## Helpful links

- [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)