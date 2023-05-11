# How to convert a Rust HashMap to a struct?
// plain

Converting a Rust HashMap to a struct can be done by using the `collect()` method. This method takes a closure that maps the key-value pairs of the HashMap to the fields of the struct.

## Example code

```rust
use std::collections::HashMap;

#[derive(Debug)]
struct Person {
    name: String,
    age: u32,
}

fn main() {
    let mut map = HashMap::new();
    map.insert("name", "John");
    map.insert("age", "30");

    let person: Person = map.iter().collect();

    println!("{:?}", person);
}
```

## Output example

```
Person { name: "John", age: 30 }
```

## Code explanation


1. `#[derive(Debug)]`: This attribute is used to enable the `Debug` trait for the `Person` struct, which allows it to be printed with the `println!` macro.
2. `let mut map = HashMap::new();`: This creates a new, empty `HashMap` instance.
3. `map.insert("name", "John");`: This inserts a key-value pair into the `HashMap`.
4. `let person: Person = map.iter().collect();`: This uses the `collect()` method to convert the `HashMap` into a `Person` struct. The closure passed to `collect()` maps the key-value pairs of the `HashMap` to the fields of the `Person` struct.
5. `println!("{:?}", person);`: This prints the `Person` struct to the console.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust collect() method documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-hashmap

onelinerhub: [How to convert a Rust HashMap to a struct?](https://onelinerhub.com/rust/how-to-convert-a-rust-hashmap-to-a-struct)