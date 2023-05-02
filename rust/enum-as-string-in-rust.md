# Enum as string in Rust
// plain

Enums in Rust can be converted to strings using the `.to_string()` method. This is useful for printing out the value of an enum in a readable format. For example, the following code creates an enum called `Fruit` with three variants, and then prints out the value of the enum as a string:
```rust
enum Fruit {
    Apple,
    Orange,
    Banana,
}

let my_fruit = Fruit::Apple;
println!("My fruit is {}", my_fruit.to_string());
```
The output of this code would be `My fruit is Apple`. The `.to_string()` method is a convenient way to convert an enum to a string, as it does not require any additional code.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust println!](https://doc.rust-lang.org/std/macro.println.html)

group: rust-enums