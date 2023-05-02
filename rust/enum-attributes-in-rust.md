# Enum attributes in Rust
// plain

Enum attributes in Rust are used to store data associated with each variant of an enum. They are declared inside the curly braces of the enum variant and can be of any type. For example, the following code creates an enum with two variants, each with an associated i32 value:
```
enum Color {
    Red(i32),
    Blue(i32),
}
```
The output of this code is:
```
Color { Red(i32), Blue(i32) }
```
The associated values can be accessed using pattern matching, as shown in the following example:
```
let color = Color::Red(5);

match color {
    Color::Red(value) => println!("The value of Red is: {}", value),
    Color::Blue(value) => println!("The value of Blue is: {}", value),
}
```
The output of this code is:
```
The value of Red is: 5
```
Enum attributes are useful for storing additional data associated with each variant of an enum. They can be accessed using pattern matching, which allows for more complex logic when dealing with enum variants.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Enum Attributes](https://doc.rust-lang.org/book/ch06-03-if-let.html#enum-attributes)
- [Pattern Matching](https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html)

group: rust-enums