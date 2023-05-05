# rust string const
// plain

A Rust `String const` is a type of constant that is used to store a string value. It is declared using the `const` keyword and is immutable, meaning it cannot be changed once declared.

## Example code

```
const MY_STRING: &str = "Hello World!";
```

## Output example

```
Hello World!
```

## Code explanation

- `const`: The keyword used to declare a constant.
- `MY_STRING`: The name of the constant.
- `&str`: The type of the constant. `&str` is a string slice, which is a reference to a string value.
- `"Hello World!"`: The value of the constant.

## Helpful links
- [Rust Documentation - Constants](https://doc.rust-lang.org/book/ch03-02-data-types.html#data-types)
- [Rust Documentation - String Slices](https://doc.rust-lang.org/book/ch04-03-slices.html#string-slices)