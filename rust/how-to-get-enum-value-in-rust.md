# How to get enum value in Rust
// plain

To get an enum value in Rust, you can use the `.into()` method. This method takes the enum variant and returns the associated value. For example, if you have an enum `Fruit` with variants `Apple` and `Orange`, you can get the associated values with `Fruit::Apple.into()` and `Fruit::Orange.into()`. The output of this method will be the associated values of the enum variants.
```rust
enum Fruit {
    Apple,
    Orange,
}

let apple_value = Fruit::Apple.into();
let orange_value = Fruit::Orange.into();

println!("Apple value: {:?}", apple_value);
println!("Orange value: {:?}", orange_value);
```
### Output example
```
Apple value: Apple
Orange value: Orange
```
### Explanation
The `.into()` method takes the enum variant and returns the associated value. In this example, `Fruit::Apple.into()` returns the associated value of the `Apple` variant, which is `Apple`, and `Fruit::Orange.into()` returns the associated value of the `Orange` variant, which is `Orange`.

### Relevant links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust Into Trait](https://doc.rust-lang.org/std/convert/trait.Into.html)
- [Rust Enum Variants](https://doc.rust-lang.org/book/ch06-03-if-let.html#matching-on-enum-variants)

group: rust-enums