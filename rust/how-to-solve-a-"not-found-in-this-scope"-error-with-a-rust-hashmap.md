# How to solve a "not found in this scope" error with a Rust HashMap?
// plain

The "not found in this scope" error is a common error when working with Rust HashMaps. To solve this error, you need to ensure that the key you are trying to access is present in the HashMap. You can do this by using the `contains_key` method, which returns a boolean value indicating whether the key is present in the HashMap.

## Example code

```rust
let mut my_map = HashMap::new();
my_map.insert("key1", "value1");

if my_map.contains_key("key1") {
    println!("key1 is present in the HashMap");
}
```

## Output example

```
key1 is present in the HashMap
```

## Code explanation

- `let mut my_map = HashMap::new();`: This line creates a new empty HashMap.
- `my_map.insert("key1", "value1");`: This line inserts a key-value pair into the HashMap.
- `if my_map.contains_key("key1") {`: This line checks if the key is present in the HashMap.
- `println!("key1 is present in the HashMap");`: This line prints a message if the key is present in the HashMap.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)