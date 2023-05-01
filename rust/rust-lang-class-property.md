# Rust lang class property
// plain

Class properties in Rust are defined using the `pub` keyword. This keyword makes the property accessible from outside the class. The syntax for defining a class property is as follows:

```
pub property_name: type
```

For example, if we want to define a class property called `name` of type `String`, we can do so as follows:

```
pub name: String
```

The following is an example of a class with a property called `name` of type `String`:

```rust
pub struct Person {
    pub name: String,
}

fn main() {
    let person = Person {
        name: String::from("John"),
    };

    println!("Name: {}", person.name);
}
```

### Output

Name: John

Explanation:

- `pub`: This keyword makes the property accessible from outside the class.
- `name`: This is the name of the property.
- `String`: This is the type of the property.
- `Person`: This is the name of the class.
- `let person = Person { name: String::from("John") };`: This line creates an instance of the `Person` class and sets the `name` property to `John`.
- `println!("Name: {}", person.name);`: This line prints the value of the `name` property.

## Helpful links:

- [Rust Documentation - Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Documentation - Modules](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)