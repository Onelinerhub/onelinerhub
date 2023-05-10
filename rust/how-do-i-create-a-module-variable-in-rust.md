# How do I create a module variable in Rust?
// plain

Creating a module variable in Rust is done by using the `static` keyword. This keyword allows you to create a variable that is accessible from anywhere within the module.

```rust
static VARIABLE_NAME: type = value;
```

For example, the following code creates a static variable called `MY_VAR` of type `i32` and assigns it the value `42`:

```rust
static MY_VAR: i32 = 42;
```

The code consists of the following parts:

- `static`: This keyword is used to declare a static variable.
- `MY_VAR`: This is the name of the variable.
- `i32`: This is the type of the variable.
- `42`: This is the value assigned to the variable.

## Helpful links

- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables)

group: rust-variables