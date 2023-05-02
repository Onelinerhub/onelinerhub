# Are there default values in Rust enums
// plain

Yes, there are default values in Rust enums. By default, the first variant of an enum is assigned the value 0, and the following variants are assigned values incrementally. For example, the following enum has the variants `Foo` and `Bar`:
```rust
enum Example {
    Foo,
    Bar,
}
```
The value of `Foo` is 0, and the value of `Bar` is 1. It is also possible to manually assign values to enum variants. For example:
```rust
enum Example {
    Foo = 5,
    Bar,
}
```
In this case, the value of `Foo` is 5, and the value of `Bar` is 6. This allows for more control over the values assigned to enum variants.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Enum Variants](https://doc.rust-lang.org/book/ch06-02-match.html#matching-on-enum-variants)
- [Enum Values](https://doc.rust-lang.org/book/ch06-02-match.html#matching-on-enum-variants)

group: rust-enums