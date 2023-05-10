# How can I create a global variable in Rust?
// plain

Global variables in Rust can be created using the `static` keyword. For example:
```
static GLOBAL_VAR: i32 = 5;
```
This creates a global variable named `GLOBAL_VAR` with the value `5`.

## Code explanation

- `static`: keyword used to create a global variable
- `GLOBAL_VAR`: name of the global variable
- `i32`: type of the global variable
- `5`: value of the global variable

## Helpful links
- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables)

group: rust-variables