# How to pretty print a struct in Rust
// plain

Pretty printing a struct in Rust is done using the `#[derive(Debug)]` annotation. This annotation allows the struct to be printed in a human-readable format.

## Example code

```rust
#[derive(Debug)]
struct Person {
    name: String,
    age: u8
}

fn main() {
    let person = Person {
        name: String::from("John"),
        age: 30
    };

    println!("{:?}", person);
}
```

## Output example

```
Person { name: "John", age: 30 }
```

## Code explanation

- `#[derive(Debug)]`: This annotation is used to enable pretty printing of the struct.
- `println!("{:?}", person)`: This macro is used to print the struct in a human-readable format.

## Helpful links
- [Rust Documentation - Derive](https://doc.rust-lang.org/rust-by-example/trait/derive.html)
- [Rust Documentation - Debug](https://doc.rust-lang.org/std/fmt/trait.Debug.html)

group: rust-struct