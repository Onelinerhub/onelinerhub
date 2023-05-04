# How to create struct from hashmap in Rust
// plain

Creating a struct from a hashmap in Rust is a simple process. To do this, you can use the `collect()` method on the hashmap. This will return a `Result` containing either an `Err` or an `Ok` value. If the `Ok` value is returned, it will contain a `HashMap<K,V>` where `K` and `V` are the types of the keys and values in the original hashmap.

## Example code

```rust
let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");

let result = map.collect::<HashMap<&str, &str>>();

match result {
    Ok(map) => println!("{:?}", map),
    Err(e) => println!("Error: {}", e),
}
```

## Output example

```
{"key1": "value1", "key2": "value2"}
```

## Code explanation

- `let mut map = HashMap::new();`: creates a new empty hashmap
- `map.insert("key1", "value1");`: inserts a key-value pair into the hashmap
- `map.collect::<HashMap<&str, &str>>();`: collects the hashmap into a `Result` containing either an `Err` or an `Ok` value
- `match result {`: matches the `Result` to determine if it is an `Err` or an `Ok` value
- `Ok(map) => println!("{:?}", map)`: if the `Ok` value is returned, it will print out the hashmap
- `Err(e) => println!("Error: {}", e)`: if the `Err` value is returned, it will print out an error message

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Collect Method Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-struct