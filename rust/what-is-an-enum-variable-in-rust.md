# What is an enum variable in Rust?
// plain

An enum variable in Rust is a type of data structure that allows a programmer to define a set of named constants. It is a type-safe way to represent a set of related values. Enums can be used to create a set of related constants, such as a set of colors or a set of days of the week.

## Example code

```
enum Color {
    Red,
    Green,
    Blue,
}

fn main() {
    let color = Color::Red;
    println!("The color is {}", color);
}
```

## Output example

```
The color is Red
```

## Code explanation


1. `enum Color {` - This line declares an enum type called Color.
2. `Red,` - This line declares a constant called Red.
3. `let color = Color::Red;` - This line assigns the constant Red to the variable color.
4. `println!("The color is {}", color);` - This line prints the value of the variable color.

## Helpful links

- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Enum Tutorial](https://www.tutorialspoint.com/rust/rust_enums.htm)

group: rust-variables