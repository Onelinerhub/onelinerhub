# How to print enum in Rust
// plain

In Rust, you can print an enum by using the `println!` macro. To do this, you must first define the enum and then use the `{:?}` formatting specifier to print it. For example, if you have an enum called `MyEnum` with two variants, `Variant1` and `Variant2`, you can print it like this:
```rust
enum MyEnum {
    Variant1,
    Variant2,
}

let my_enum = MyEnum::Variant1;
println!("{:?}", my_enum);
```
This will print `Variant1` to the console. The `{:?}` formatting specifier is a shorthand for the `Debug` trait, which is used to print out the value of an enum.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust println! macro](https://doc.rust-lang.org/std/macro.println.html)
- [Rust Debug trait](https://doc.rust-lang.org/std/fmt/trait.Debug.html)

group: rust-enums