# How to cast enum in Rust
// plain

In Rust, you can cast an enum to a number using the `as` keyword. For example, if you have an enum `Fruit` with variants `Apple`, `Orange`, and `Banana`, you can cast it to an integer like this:
```rust
enum Fruit {
    Apple,
    Orange,
    Banana,
}

let my_fruit = Fruit::Apple;
let my_fruit_as_int = my_fruit as i32;
```
The output of this code would be `my_fruit_as_int = 0`. This is because the variants of the enum are assigned values starting from 0.

You can also cast a number to an enum using the `from` keyword. For example, if you have the same enum `Fruit` as before, you can cast an integer to it like this:
```rust
let my_int = 2;
let my_int_as_fruit = Fruit::from(my_int);
```
The output of this code would be `my_int_as_fruit = Fruit::Banana`.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Casting](https://doc.rust-lang.org/book/ch06-02-match.html#casting-values-to-other-types)
- [Rust From Trait](https://doc.rust-lang.org/std/convert/trait.From.html)

group: rust-enums