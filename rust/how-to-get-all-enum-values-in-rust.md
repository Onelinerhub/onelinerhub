# How to get all enum values in Rust
// plain

To get all enum values in Rust, you can use the `std::mem::size_of_val` function to get the size of the enum type and then use a loop to iterate through all the possible values. For example, if you have an enum type called `MyEnum` with 4 variants, you can use the following code to get all the enum values:
```rust
let enum_size = std::mem::size_of_val(&MyEnum::Variant1);
for i in 0..enum_size {
    let enum_value = MyEnum::from_u8(i).unwrap();
    println!("{:?}", enum_value);
}
```
This will print out all the enum values, e.g. `Variant1`, `Variant2`, `Variant3`, and `Variant4`.

The `std::mem::size_of_val` function returns the size of the enum type in bytes, which is then used to iterate through all the possible values. The `MyEnum::from_u8` function is used to convert the index of the loop into an enum value. The `unwrap` function is used to handle any errors that may occur when converting the index to an enum value.

## Helpful links
- [std::mem::size_of_val](https://doc.rust-lang.org/std/mem/fn.size_of_val.html)
- [Enum::from_u8](https://doc.rust-lang.org/std/primitive.u8.html#method.from_u8)
- [Result::unwrap](https://doc.rust-lang.org/std/result/enum.Result.html#method.unwrap)

group: rust-enums