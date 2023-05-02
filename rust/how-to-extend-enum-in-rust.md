# How to extend enum in Rust
// plain

Enums in Rust can be extended by adding additional variants to the enum definition. This can be done by using the `enum` keyword followed by the name of the enum and then the variants. For example, to extend the `Fruit` enum with a new variant `Mango`, the code would look like this:
```rust
enum Fruit {
Apple,
Orange,
Mango,
}
```
The output of this code would be:
```
Fruit { Apple, Orange, Mango }
```
The code defines a new enum called `Fruit` with three variants: `Apple`, `Orange`, and `Mango`. The variants can then be used in code to represent different values. For example, the following code would print out the string `Mango`:
```rust
let fruit = Fruit::Mango;
println!("{}", fruit);
```
The output of this code would be:
```
Mango
```
For more information on enums in Rust, please refer to the [Rust Enums documentation](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html).

group: rust-enums