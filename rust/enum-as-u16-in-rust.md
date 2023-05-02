# Enum as u16 in Rust
// plain

Enum in Rust is a type that allows you to define a set of named constants. It can be used to represent a set of related values, such as the days of the week, or a set of flags. Enums can also be used to define a type that can be stored as a 16-bit unsigned integer (u16). To define an enum as a u16, you can use the #[repr(u16)] attribute. For example:

```rust
#[repr(u16)]
enum MyEnum {
    Value1 = 1,
    Value2 = 2,
    Value3 = 3,
}
```

This will define an enum that can be stored as a u16, with the values Value1, Value2, and Value3. The values can be accessed using the enum's name, followed by the value's name, such as MyEnum::Value1.

The output of this ## Code example will be:

```
Value1 = 1
Value2 = 2
Value3 = 3
```

The #[repr(u16)] attribute tells the Rust compiler to store the enum as a u16, instead of the default 32-bit unsigned integer (u32). This can be useful if you need to store the enum in a memory-constrained environment, or if you need to store the enum in a file or database.

## Helpful links

- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Repr Attribute](https://doc.rust-lang.org/reference/attributes/type_system.html#the-repr-attribute)
- [Unsigned Integer Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#integer-types)

group: rust-enums