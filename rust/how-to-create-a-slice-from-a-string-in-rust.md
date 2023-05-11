# How to create a slice from a string in Rust?
// plain

Creating a slice from a string in Rust is a simple process. The `&str` type is a slice that points to a specific point in a `String` type. To create a `&str` from a `String`, you can use the `as_str()` method.

```rust
let my_string = String::from("Hello World!");
let my_slice = my_string.as_str();
println!("{}", my_slice);
```

## Output example

```
Hello World!
```

The code above creates a `String` type called `my_string` and then creates a `&str` type called `my_slice` from `my_string` using the `as_str()` method. Finally, the `println!` macro is used to print the contents of `my_slice`.

## Code explanation

- `let my_string = String::from("Hello World!");`: creates a `String` type called `my_string`
- `let my_slice = my_string.as_str();`: creates a `&str` type called `my_slice` from `my_string` using the `as_str()` method
- `println!("{}", my_slice);`: prints the contents of `my_slice` using the `println!` macro

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Documentation - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)

group: rust-slice