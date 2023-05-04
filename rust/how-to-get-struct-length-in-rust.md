# How to get struct length in Rust
// plain

Structs in Rust are collections of related data, similar to a class in other languages. To get the length of a struct, you can use the `std::mem::size_of` function.

```rust
use std::mem::size_of;

struct Person {
    name: String,
    age: u8
}

fn main() {
    let person = Person {
        name: String::from("John"),
        age: 30
    };

    println!("Size of Person struct is {} bytes", size_of::<Person>());
}
```

## Output example

```
Size of Person struct is 24 bytes
```

The code above uses the `size_of` function to get the size of the `Person` struct. The `size_of` function takes a type parameter, in this case `Person`, and returns the size of the struct in bytes.

## Code explanation

- `use std::mem::size_of;`: imports the `size_of` function from the `std::mem` module.
- `struct Person { ... }`: defines a struct with two fields, `name` and `age`.
- `size_of::<Person>()`: calls the `size_of` function with the `Person` type as a parameter.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)

group: rust-struct