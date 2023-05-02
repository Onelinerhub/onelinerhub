# How to use fmt for enum in Rust
// plain

To use fmt for enum in Rust, you can use the following template:
```rust
#[derive(Debug)]
enum EnumName {
    Variant1,
    Variant2,
    Variant3,
}

fn main() {
    let enum_instance = EnumName::Variant1;
    println!("{:?}", enum_instance);
}
```
The output of this code will be:
```
Variant1
```
The `#[derive(Debug)]` attribute allows us to use the `println!` macro to print out the enum instance. The `:?` format specifier is used to print out the enum instance in a debug format.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust fmt](https://doc.rust-lang.org/std/fmt/)
- [Rust println!](https://doc.rust-lang.org/std/macro.println.html)

group: rust-enums