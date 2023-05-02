# How to derive enum from in Rust
// plain

Enums in Rust are used to define a set of named constants. To derive an enum from a struct, you must first define the enum and then use the #[derive] attribute to specify the desired behavior. For example, the following code defines an enum called Color and derives the PartialEq and Debug traits from it:
```rust
#[derive(PartialEq, Debug)]
enum Color {
    Red,
    Blue,
    Green,
}
```
The #[derive] attribute allows you to automatically implement certain traits for the enum. In this case, the PartialEq and Debug traits are implemented, which allows you to compare two Color values and print out a debug representation of the Color value.

Output example:
```
let color1 = Color::Red;
let color2 = Color::Blue;

assert_eq!(color1, color1);
assert_ne!(color1, color2);

println!("{:?}", color1);
```
### Output
```
Red
```
## Explanation

The code first defines two Color values, `color1` and `color2`, and then uses the `assert_eq!` and `assert_ne!` macros to compare them. The `assert_eq!` macro will check if the two values are equal, and the `assert_ne!` macro will check if the two values are not equal. Finally, the `println!` macro is used to print out a debug representation of the `color1` value.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Deriving Traits](https://doc.rust-lang.org/book/ch10-02-traits.html#derivable-traits)
- [Rust Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)

group: rust-enums