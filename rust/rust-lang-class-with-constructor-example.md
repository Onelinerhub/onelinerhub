# Rust lang class with constructor example
// plain

A constructor in Rust is a function that is called when an instance of a struct is created. It is used to initialize the fields of the struct with the given values.

Below is an example of a Rust class with a constructor:

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
}

fn main() {
    let person = Person::new(String::from("John"), 30);
    println!("{} is {} years old", person.name, person.age);
}
```

### Output

John is 30 years old

Explanation:

1. The `struct Person` defines a struct with two fields, `name` and `age`, both of type `String` and `u8` respectively.
2. The `impl Person` block defines an implementation block for the `Person` struct.
3. The `fn new` function is the constructor for the `Person` struct. It takes two parameters, `name` and `age`, both of type `String` and `u8` respectively.
4. The `let person` statement creates an instance of the `Person` struct using the `Person::new` constructor.
5. The `println!` statement prints out the name and age of the `person` instance.

## Helpful links:

1. [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
2. [Rust Constructors](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#defining-methods-with-the-same-name-as-the-struct)