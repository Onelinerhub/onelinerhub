# How to add an entry to a Rust HashMap?
// plain

Adding an entry to a Rust HashMap is a simple process. The following example code block shows how to add a key-value pair to a HashMap:

```
let mut map = HashMap::new();
map.insert("key", "value");
```

The output of the above code will be an empty HashMap with the key-value pair `("key", "value")` added to it.

## Code explanation


1. `let mut map = HashMap::new();` - This line creates a new empty HashMap.
2. `map.insert("key", "value");` - This line adds the key-value pair `("key", "value")` to the HashMap.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to add an entry to a Rust HashMap?](https://onelinerhub.com/rust/how-to-add-an-entry-to-a-rust-hashmap)