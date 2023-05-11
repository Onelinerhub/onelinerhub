# Rust HashMap example
// plain

Rust's `HashMap` is a data structure that stores key-value pairs. It is a hash table implementation of the `Map` trait.

## Example code

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name);

println!("{:?}", score);
```

## Output example

```
Some(10)
```

## Code explanation


1. `use std::collections::HashMap;` - This imports the `HashMap` type from the `std::collections` module.

2. `let mut scores = HashMap::new();` - This creates a new empty `HashMap` called `scores`.

3. `scores.insert(String::from("Blue"), 10);` - This inserts a key-value pair into the `HashMap`, with the key being a `String` containing the value "Blue" and the value being an `i32` containing the value 10.

4. `let team_name = String::from("Blue");` - This creates a `String` containing the value "Blue".

5. `let score = scores.get(&team_name);` - This retrieves the value associated with the key `team_name` from the `HashMap`.

6. `println!("{:?}", score);` - This prints the value associated with the key `team_name` from the `HashMap`.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [Rust HashMap example](https://onelinerhub.com/rust/rust-hashmap-example)