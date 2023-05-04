# How to iterate through hashmap keys in Rust
// plain

Iterating through a HashMap in Rust can be done using the `iter()` method. This method returns an iterator over the key-value pairs of the HashMap. The following example code block shows how to iterate through the keys of a HashMap:

```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

for (key, _) in map.iter() {
    println!("{}", key);
}
```

This code will output:
```
a
b
c
```

The code works by first creating a new HashMap and inserting three key-value pairs. Then, the `iter()` method is used to get an iterator over the key-value pairs. Finally, a `for` loop is used to iterate over the iterator and print out the keys.

## Code explanation


1. `let mut map = HashMap::new();`: creates a new empty HashMap.
2. `map.insert("a", 1);`: inserts a key-value pair into the HashMap.
3. `map.iter()`: returns an iterator over the key-value pairs of the HashMap.
4. `for (key, _) in map.iter()`: iterates over the iterator and assigns the key to the `key` variable.
5. `println!("{}", key);`: prints out the key.

## Helpful links

- [HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Iterator documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-loops