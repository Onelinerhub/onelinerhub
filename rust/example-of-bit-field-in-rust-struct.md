# Example of bit field in Rust struct
// plain

A bit field is a data structure used to store multiple boolean values in a single data type. In Rust, bit fields can be used to create a struct that stores multiple boolean values in a single data type.

## Example code

```rust
struct MyStruct {
    a: bool,
    b: bool,
    c: bool,
    d: bool,
}
```

This code creates a struct called `MyStruct` that contains four boolean fields, `a`, `b`, `c`, and `d`.

## Code explanation

- `struct MyStruct`: This is the declaration of the struct.
- `a: bool,`: This is the declaration of the first boolean field, `a`.
- `b: bool,`: This is the declaration of the second boolean field, `b`.
- `c: bool,`: This is the declaration of the third boolean field, `c`.
- `d: bool`: This is the declaration of the fourth boolean field, `d`.

## Helpful links
- [Rust Bit Fields](https://doc.rust-lang.org/book/ch19-03-advanced-features.html#using-bit-fields-to-pack-data-tightly)

group: rust-struct