# How do I declare a static function variable in Rust?
// plain

A static function variable in Rust is declared using the `static` keyword. This keyword is used to declare a variable that is accessible from any scope within the program.

## Example

```
static MY_VAR: i32 = 5;
```

This declares a static variable named `MY_VAR` of type `i32` with a value of `5`.

## Code explanation

- `static`: keyword used to declare a static variable
- `MY_VAR`: name of the static variable
- `i32`: type of the static variable
- `5`: value of the static variable

## Helpful links
- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables)

group: rust-variables