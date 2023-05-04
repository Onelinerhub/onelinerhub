# How to iterate a map in Rust
// plain

Iterating a map in Rust is done using the `for` loop. The syntax for this is as follows:

```
for (key, value) in &map {
    // code block
}
```

The code block will be executed for each key-value pair in the map. The `key` and `value` variables will contain the key and value of the current iteration.

- `for`: looping construct
- `(key, value)`: variables to store the key and value of the current iteration
- `&map`: reference to the map

## Helpful links
- [Rust Documentation - Iterating over a map](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.iter)

group: rust-loops