# How to update struct in Rust
// plain

Updating a struct in Rust is a simple process. To do so, you must first create a mutable reference to the struct. Then, you can use the dot notation to access and update the fields of the struct.

```rust
struct Person {
    name: String,
    age: u8
}

fn main() {
    let mut person = Person {
        name: String::from("John"),
        age: 30
    };

    person.age = 31;

    println!("{} is now {} years old", person.name, person.age);
}
```

## Output example

```
John is now 31 years old
```

## Code explanation


1. `struct Person { name: String, age: u8 }` - This is the definition of the `Person` struct, which contains two fields: `name` of type `String` and `age` of type `u8`.

2. `let mut person = Person { name: String::from("John"), age: 30 }` - This creates a mutable reference to a `Person` struct with the name `John` and age `30`.

3. `person.age = 31` - This updates the `age` field of the `person` struct to `31`.

4. `println!("{} is now {} years old", person.name, person.age)` - This prints out the updated age of the `person` struct.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Mutability](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#mutable-references)

group: rust-struct