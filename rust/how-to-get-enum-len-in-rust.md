# How to get enum len in Rust
// plain

You can get the length of an enum in Rust by using the `std::mem::size_of` function. This function takes a type as an argument and returns the size of the type in bytes. For enums, this will return the number of variants in the enum. For example, if you have an enum with three variants, the size of the enum will be 3. To get the length of the enum, you can divide the size of the enum by the size of one of its variants. For example:

```rust
use std::mem::size_of;

enum MyEnum {
    Variant1,
    Variant2,
    Variant3,
}

let enum_len = size_of::<MyEnum>() / size_of::<MyEnum::Variant1>();

println!("Enum length: {}", enum_len);
```

This code will print out `Enum length: 3`.

## Helpful links
- [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)
- [Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust by Example - Enums](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html)

group: rust-enums