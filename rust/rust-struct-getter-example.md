# Rust struct getter example
// plain

A `struct` in Rust is a custom data type that allows you to store related pieces of data together. It is similar to a class in other languages.

## Example code

```rust
struct Person {
    name: String,
    age: u8
}

fn main() {
    let person = Person {
        name: String::from("John"),
        age: 30
    };

    println!("Name: {}", person.name);
    println!("Age: {}", person.age);
}
```

## Output example

```
Name: John
Age: 30
```

## Code explanation

- `struct Person`: This is the definition of the `Person` struct. It contains two fields, `name` of type `String` and `age` of type `u8`.
- `let person = Person`: This creates an instance of the `Person` struct with the given values.
- `println!("Name: {}", person.name);`: This prints the value of the `name` field of the `person` instance.
- `println!("Age: {}", person.age);`: This prints the value of the `age` field of the `person` instance.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust println! macro](https://doc.rust-lang.org/std/macro.println.html)

group: rust-struct