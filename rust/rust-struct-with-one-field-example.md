# Rust struct with one field example
// plain

A `struct` in Rust is a custom data type that can contain multiple fields. Here is an example of a `struct` with one field:

```rust
struct Point {
    x: i32,
}
```

This `struct` is called `Point` and it has one field called `x` which is of type `i32`. We can create an instance of this `struct` like this:

```rust
let point = Point { x: 0 };
```

This creates a `Point` instance with the `x` field set to `0`.

Parts of the code:

- `struct Point {`: This is the start of the `struct` definition.
- `x: i32,`: This is the field of the `struct`. It is called `x` and is of type `i32`.
- `let point = Point { x: 0 };`: This creates an instance of the `struct` with the `x` field set to `0`.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)

group: rust-struct