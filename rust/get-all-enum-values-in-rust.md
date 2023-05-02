# Get all enum values in Rust
// plain

In Rust, enum values can be accessed using the `variants()` method. This method returns an iterator over all the variants of the enum. To get all the enum values, the iterator can be collected into a vector. The ## Code example below shows how to do this:
```rust
enum Color {
    Red,
    Green,
    Blue,
}

fn main() {
    let colors: Vec<Color> = Color::variants().collect();
    println!("{:?}", colors);
}
```
The output of this code is:
```
[Red, Green, Blue]
```
The `variants()` method returns an iterator over all the variants of the enum. This iterator is then collected into a vector, which is then printed out. The `{:?}` format specifier is used to print out the vector in a readable format.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Iterators](https://doc.rust-lang.org/book/ch13-00-functional-features.html#iterators)
- [Rust Formatting](https://doc.rust-lang.org/std/fmt/)

group: rust-enums