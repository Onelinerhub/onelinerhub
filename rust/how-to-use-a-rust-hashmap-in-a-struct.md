# How to use a Rust HashMap in a struct?
// plain

A Rust HashMap can be used in a struct by declaring a field of type `HashMap<K, V>` where `K` is the type of the key and `V` is the type of the value.

## Example code

```rust
use std::collections::HashMap;

struct MyStruct {
    map: HashMap<String, i32>,
}

fn main() {
    let mut my_struct = MyStruct {
        map: HashMap::new(),
    };
    my_struct.map.insert("key".to_string(), 1);
    println!("{:?}", my_struct);
}
```

## Output example

```
MyStruct { map: {"key": 1} }
```

## Code explanation


1. `use std::collections::HashMap;`: This imports the `HashMap` type from the `std::collections` module.

2. `map: HashMap<String, i32>`: This declares a field of type `HashMap<String, i32>` in the `MyStruct` struct.

3. `HashMap::new()`: This creates a new empty `HashMap` instance.

4. `my_struct.map.insert("key".to_string(), 1);`: This inserts a key-value pair into the `HashMap` instance.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to use a Rust HashMap in a struct?](https://onelinerhub.com/rust/how-to-use-a-rust-hashmap-in-a-struct)