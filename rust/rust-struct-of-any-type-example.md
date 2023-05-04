# Rust struct of any type example
// plain

A `struct` is a custom data type in Rust that allows you to group related data together. It is similar to a class in other languages. Here is an example of a `struct` that stores information about a person:

```rust
struct Person {
    name: String,
    age: u8
}
```

This `struct` has two fields, `name` and `age`, both of which are of type `String` and `u8` respectively. The `name` field stores the person's name as a `String` and the `age` field stores the person's age as an `u8` (unsigned 8-bit integer).

To create an instance of this `struct`, we can use the `new` keyword:

```rust
let person = Person {
    name: String::from("John"),
    age: 30
};
```

This creates a `Person` instance with the name `John` and age `30`. We can then access the fields of this instance using dot notation:

```rust
println!("Name: {}", person.name);
println!("Age: {}", person.age);
```

This will print out the following:

```
Name: John
Age: 30
```

We can also create methods on our `struct`s to perform operations on the data they contain. For example, we could create a `greet` method that prints out a greeting for the person:

```rust
impl Person {
    fn greet(&self) {
        println!("Hello, my name is {} and I am {} years old.", self.name, self.age);
    }
}
```

We can then call this method on our `person` instance:

```rust
person.greet();
```

This will print out the following:

```
Hello, my name is John and I am 30 years old.
```

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Impl Blocks](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)

group: rust-struct