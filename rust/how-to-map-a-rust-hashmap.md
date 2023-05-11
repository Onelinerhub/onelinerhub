# How to map a Rust HashMap?
// plain

Mapping a Rust HashMap is a simple process. It involves creating a new HashMap, inserting key-value pairs, and then iterating over the HashMap to access the values.

## Example code

```
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert("key1", "value1");
    map.insert("key2", "value2");

    for (key, value) in &map {
        println!("{}: {}", key, value);
    }
}
```

## Output example

```
key1: value1
key2: value2
```

## Code explanation


1. `use std::collections::HashMap;`: This imports the HashMap type from the standard library.

2. `let mut map = HashMap::new();`: This creates a new, empty HashMap.

3. `map.insert("key1", "value1");`: This inserts a key-value pair into the HashMap.

4. `for (key, value) in &map {`: This iterates over the HashMap, giving access to the keys and values.

5. `println!("{}: {}", key, value);`: This prints out the key and value for each iteration.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to map a Rust HashMap?](https://onelinerhub.com/rust/how-to-map-a-rust-hashmap)