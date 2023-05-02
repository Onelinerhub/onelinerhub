# How to iterate enum in Rust
// plain

Enumerations in Rust can be iterated over using the `.iter()` method. This method returns an iterator over all variants of the enum. For example, the following code iterates over an enum called `Fruit` and prints out the variants:
```rust
enum Fruit {
    Apple,
    Orange,
    Banana,
}

for fruit in Fruit::iter() {
    println!("{:?}", fruit);
}
```

The output of this code would be:
```
Apple
Orange
Banana
```

The `.iter()` method returns an iterator over all variants of the enum, which can then be used in a loop to iterate over each variant. The `println!` macro is used to print out the variants of the enum.

For more information on enumerations in Rust, see the [Rust Book](https://doc.rust-lang.org/book/ch06-00-enums.html) and the [Rust Enums Guide](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html).

group: rust-enums