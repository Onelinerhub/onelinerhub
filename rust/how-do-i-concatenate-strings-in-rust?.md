# How do I concatenate strings in Rust?
// plain

Strings in Rust can be concatenated using the `+` operator. For example:

```
let s1 = "Hello";
let s2 = "World";
let s3 = s1 + " " + s2;
println!("{}", s3);
```

This will output `Hello World`.

## Code explanation


- `let s1 = "Hello";` - This declares a string variable `s1` and assigns it the value `Hello`.
- `let s2 = "World";` - This declares a string variable `s2` and assigns it the value `World`.
- `let s3 = s1 + " " + s2;` - This declares a string variable `s3` and assigns it the value of `s1` concatenated with a space and `s2`.
- `println!("{}", s3);` - This prints the value of `s3` to the console.

## Helpful links

- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Operators](https://doc.rust-lang.org/book/ch03-02-operators-and-overloading.html)