# Enum as int in Rust
// plain

Enums in Rust can be used to represent a set of named constants, such as the four seasons. Enums can also be used to represent a set of numeric values, such as a set of integer values. To use an enum as an integer, you can use the #[repr(int)] attribute. This attribute will cause the enum to be represented as an integer in the compiled code. For example:
```rust
#[repr(int)]
enum Seasons {
    Spring = 0,
    Summer = 1,
    Fall = 2,
    Winter = 3,
}
```
In this example, the enum is represented as an integer in the compiled code, with Spring being 0, Summer being 1, Fall being 2, and Winter being 3. This allows you to use the enum values in arithmetic operations, such as adding or subtracting.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust #[repr(int)]](https://doc.rust-lang.org/reference/attributes/type_system/repr.html#reprint)
- [Rust Enum Arithmetic](https://doc.rust-lang.org/book/ch06-02-match.html#matching-with-enum-values)

group: rust-enums