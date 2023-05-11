# How to loop through a Rust HashMap?
// plain

Looping through a Rust HashMap can be done using the `iter()` method. This method returns an iterator over the key-value pairs of the map. The following example code block shows how to loop through a HashMap and print out the key-value pairs:

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert("a", 1);
    map.insert("b", 2);
    map.insert("c", 3);

    for (key, value) in map.iter() {
        println!("{}: {}", key, value);
    }
}
```

## Output example

```
a: 1
b: 2
c: 3
```

The code above consists of the following parts:

1. `use std::collections::HashMap;` - imports the `HashMap` type from the `std::collections` module.
2. `let mut map = HashMap::new();` - creates a new empty `HashMap` and stores it in the `map` variable.
3. `map.insert("a", 1);` - inserts a key-value pair into the `map` variable.
4. `for (key, value) in map.iter() {` - starts a loop over the key-value pairs of the `map` variable.
5. `println!("{}: {}", key, value);` - prints out the key-value pairs.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to loop through a Rust HashMap?](https://onelinerhub.com/rust/how-to-loop-through-a-rust-hashmap)