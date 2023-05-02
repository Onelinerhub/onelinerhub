# Using enum match in Rust
// plain

Enum match in Rust is a powerful tool for pattern matching. It allows you to match on the value of an enum and execute code based on the value. For example, the following ## Code example uses enum match to match on the value of a Color enum and print a message based on the value:
```rust
enum Color {
    Red,
    Blue,
    Green,
}

fn main() {
    let color = Color::Red;

    match color {
        Color::Red => println!("The color is Red"),
        Color::Blue => println!("The color is Blue"),
        Color::Green => println!("The color is Green"),
    }
}
```

The output of this ## Code example is:
```
The color is Red
```

The ## Code example uses the enum match syntax to match on the value of the Color enum. If the value of the enum is Red, the code block associated with the Color::Red match arm is executed. If the value of the enum is Blue, the code block associated with the Color::Blue match arm is executed, and so on.

## Helpful links
- [Enum Match in Rust](https://doc.rust-lang.org/book/ch06-02-match.html#matching-on-enum-variants)
- [Enum Match in Rust Tutorial](https://www.tutorialspoint.com/rust/rust_enum_match.htm)
- [Enum Match in Rust Cheat Sheet](https://cheats.rs/#enum-match)

group: rust-enums