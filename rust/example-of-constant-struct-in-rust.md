# Example of constant struct in Rust
// plain

A constant struct in Rust is a struct that is declared with the `const` keyword. This allows the struct to be used in a constant expression, meaning that it can be used in places where only constant values are allowed.

## Example code

```rust
const MY_STRUCT: MyStruct = MyStruct {
    field1: "value1",
    field2: "value2",
};
```

This example declares a constant struct named `MY_STRUCT` of type `MyStruct` with two fields, `field1` and `field2`.

## Code explanation

- `const`: The keyword used to declare a constant struct.
- `MY_STRUCT`: The name of the constant struct.
- `MyStruct`: The type of the constant struct.
- `field1` and `field2`: The fields of the constant struct.
- `"value1"` and `"value2"`: The values of the fields of the constant struct.

## Helpful links
- [Rust Documentation - Constants](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#constants)

group: rust-struct