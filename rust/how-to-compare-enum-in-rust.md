# How to compare enum in Rust
// plain

Enums in Rust can be compared using the `==` operator. For example, if you have an enum `Fruit` with variants `Apple`, `Orange`, and `Banana`, you can compare two enum values like this:
```rust
let fruit1 = Fruit::Apple;
let fruit2 = Fruit::Orange;

if fruit1 == fruit2 {
    println!("The fruits are the same!");
} else {
    println!("The fruits are different!");
}
```

The output of this code would be:
```
The fruits are different!
```

The `==` operator compares the variants of the enum, so in this case it would compare `Apple` and `Orange` and return `false`.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Equality Operator](https://doc.rust-lang.org/std/primitive.bool.html#equality-operators)
- [Rust Enum Comparison](https://stackoverflow.com/questions/41009072/how-to-compare-enums-in-rust)

group: rust-enums