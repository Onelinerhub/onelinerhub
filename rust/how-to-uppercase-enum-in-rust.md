# How to uppercase enum in Rust
// plain

To uppercase an enum in Rust, you can use the `to_uppercase()` method on the enum's `Variant` type. For example, if you have an enum called `MyEnum` with variants `Variant1` and `Variant2`, you can uppercase them like this:
```rust
let my_enum = MyEnum::Variant1;
let uppercase_enum = my_enum.variant().to_uppercase();
```
This will set `uppercase_enum` to `VARIANT1`.

The `to_uppercase()` method is part of the `std::string::ToString` trait, which is implemented for all `Variant` types. This means that you can use `to_uppercase()` on any enum variant.

Example ### Output
```
uppercase_enum = VARIANT1
```

## Explanation
 The `let my_enum = MyEnum::Variant1;` line creates a new `MyEnum` enum with the `Variant1` variant. The `let uppercase_enum = my_enum.variant().to_uppercase();` line then calls the `to_uppercase()` method on the `Variant1` variant, which returns the uppercase version of the variant.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust Strings](https://doc.rust-lang.org/std/string/index.html)
- [Rust Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)

group: rust-enums