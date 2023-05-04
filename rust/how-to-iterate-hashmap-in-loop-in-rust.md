# How to iterate hashmap in loop in Rust
// plain

Iterating over a HashMap in Rust can be done using a `for` loop. The syntax for this is as follows:

```
for (key, value) in &hashmap {
    // do something with key and value
}
```

The ## Code explanation


- `for`: the keyword used to start a loop
- `(key, value)`: the variables used to store the key and value of each entry in the HashMap
- `&hashmap`: the reference to the HashMap being iterated over
- `// do something with key and value`: the code that will be executed for each entry in the HashMap

## Helpful links

- [Rust Documentation - Iterating over a HashMap](https://doc.rust-lang.org/std/collections/hash_map/enum.Entry.html#iterating-over-a-hashmap)

group: rust-loops