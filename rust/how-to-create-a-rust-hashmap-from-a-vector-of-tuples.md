# How to create a Rust HashMap from a vector of tuples?
// plain

Creating a Rust HashMap from a vector of tuples is a simple process. The following example code creates a HashMap from a vector of tuples:

```rust
let mut map = HashMap::new();
let v = vec![(1, "a"), (2, "b"), (3, "c")];

for (key, value) in v {
    map.insert(key, value);
}
```

The output of the example code is:
```
HashMap { 1: "a", 2: "b", 3: "c" }
```

## Code explanation


1. `let mut map = HashMap::new();` - This creates a new, empty HashMap.
2. `let v = vec![(1, "a"), (2, "b"), (3, "c")];` - This creates a vector of tuples.
3. `for (key, value) in v {` - This starts a loop that iterates over each tuple in the vector.
4. `map.insert(key, value);` - This inserts the key and value from the tuple into the HashMap.
5. `}` - This ends the loop.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Vector Documentation](https://doc.rust-lang.org/std/vec/struct.Vec.html)

group: rust-hashmap

onelinerhub: [How to create a Rust HashMap from a vector of tuples?](https://onelinerhub.com/rust/how-to-create-a-rust-hashmap-from-a-vector-of-tuples)