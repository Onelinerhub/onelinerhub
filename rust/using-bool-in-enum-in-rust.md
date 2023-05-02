# Using bool in enum in Rust
// plain

Yes, it is possible to use bool in enum in Rust. This can be done by using the #[repr(bool)] attribute on the enum. This attribute allows the enum to be represented as a bool type in memory. For example, the following code creates an enum with two variants, True and False, and assigns them the values of true and false respectively:
```rust
#[repr(bool)]
enum BoolEnum {
    True = true,
    False = false,
}
```
The output of this code is a BoolEnum type that can be used like a bool type. For example, the following code prints out the value of a BoolEnum variable:

```rust
let b = BoolEnum::True;
println!("{}", b);
```

Output example:
```
true
```

The #[repr(bool)] attribute allows the enum to be represented as a bool type in memory, which makes it easier to use the enum in comparison operations. This is useful when dealing with boolean values that need to be represented in an enum.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [#[repr(bool)]](https://doc.rust-lang.org/std/primitive.bool.html#representations)
- [Rust Enum Tutorial](https://www.tutorialspoint.com/rust/rust_enums.htm)

group: rust-enums