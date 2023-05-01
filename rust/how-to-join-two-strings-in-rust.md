# How to join two strings in Rust
// plain

Joining two strings in Rust can be done using the `+` operator. The following ## Code example shows how to join two strings:

```rust
let string1 = "Hello";
let string2 = "World";
let joined_string = string1 + " " + string2;
println!("{}", joined_string);
```
### Output
```
Hello World
```

Explanation:
- The `let` keyword is used to declare a variable.
- The `string1` and `string2` variables are declared and assigned the strings "Hello" and "World" respectively.
- The `+` operator is used to join the two strings.
- The `println!` macro is used to print the joined string to the console.
- The `{}` placeholder is used to specify the value of the `joined_string` variable.

## Helpful links:
- [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)