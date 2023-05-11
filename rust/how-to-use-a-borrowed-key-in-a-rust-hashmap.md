# How to use a borrowed key in a Rust HashMap?
// plain

Using a borrowed key in a Rust HashMap is easy.

```
use std::collections::HashMap;

let mut map = HashMap::new();

let key = "key";
let value = "value";

map.insert(key, value);

let borrowed_key = &key;
let borrowed_value = map.get(borrowed_key);

println!("{:?}", borrowed_value);
```

## Output example

```
Some("value")
```

1. `let mut map = HashMap::new();` - Create a new empty HashMap.
2. `let key = "key"; let value = "value";` - Create a key and value to insert into the HashMap.
3. `map.insert(key, value);` - Insert the key and value into the HashMap.
4. `let borrowed_key = &key;` - Create a borrowed reference to the key.
5. `let borrowed_value = map.get(borrowed_key);` - Get the value from the HashMap using the borrowed key.
6. `println!("{:?}", borrowed_value);` - Print the value.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to use a borrowed key in a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-a-borrowed-key-in-a-rust-hashmap)