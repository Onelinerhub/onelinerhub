# How to create enum from int in Rust
// plain

Enums in Rust are used to define a set of named constants. To create an enum from an integer, you can use the From trait. This trait allows you to convert an integer into an enum variant. The following ## Code example shows how to create an enum from an integer:
```
enum Color {
    Red,
    Green,
    Blue,
}

let color_int = 2;
let color = Color::from(color_int);

println!("The color is: {:?}", color);
```

### Output example
The color is: Blue

### Explanation
The ## Code example starts by defining an enum called Color with three variants: Red, Green, and Blue. Then, an integer is assigned to the variable color_int. The From trait is used to convert the integer into an enum variant. Finally, the println! macro is used to print the enum variant to the console.

### Relevant links
[Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)

[From Trait](https://doc.rust-lang.org/std/convert/trait.From.html)

[Println! Macro](https://doc.rust-lang.org/std/macro.println.html)

group: rust-enums