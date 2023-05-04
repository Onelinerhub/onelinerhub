# How to create struct in Rust
// plain

Structs are a way to create custom data types in Rust. They are similar to classes in other languages. Structs are created using the `struct` keyword, followed by the name of the struct and a set of fields.

```rust
struct Person {
    name: String,
    age: u8
}
```

This example creates a `Person` struct with two fields, `name` and `age`, both of which are of type `String` and `u8` respectively.

- `struct`: keyword used to create a struct
- `Person`: name of the struct
- `name`: field of type `String`
- `age`: field of type `u8`

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)

group: rust-struct