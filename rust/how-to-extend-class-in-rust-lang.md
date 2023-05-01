# How to extend class in Rust lang
// plain

In Rust, you can extend a class by using the `impl` keyword. This allows you to add methods and fields to an existing class. Here is an example of extending a class in Rust:

```
struct Person {
    name: String,
    age: u8
}

impl Person {
    fn new(name: String, age: u8) -> Person {
        Person {
            name,
            age
        }
    }

    fn get_name(&self) -> &String {
        &self.name
    }
}

fn main() {
    let person = Person::new("John".to_string(), 30);
    println!("Name: {}", person.get_name());
}
```

### Output

Name: John

Explanation:

- `struct Person`: This defines a struct called `Person` with two fields, `name` and `age`.
- `impl Person`: This is the `impl` block which allows us to extend the `Person` struct.
- `fn new`: This is a constructor method which takes two parameters, `name` and `age`, and returns a `Person` instance.
- `fn get_name`: This is a method which takes a `&self` parameter and returns a reference to the `name` field of the `Person` instance.
- `let person`: This creates a new `Person` instance using the `new` constructor method.
- `println!`: This prints out the `name` field of the `Person` instance.

## Helpful links:

- [Rust Documentation - Impl Blocks](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#impl-blocks)
- [Rust Documentation - Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)