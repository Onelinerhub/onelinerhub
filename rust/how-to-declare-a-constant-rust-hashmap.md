# How to declare a constant Rust HashMap?
// plain

A constant Rust HashMap can be declared using the `const` keyword.

```rust
const MY_HASHMAP: HashMap<&str, i32> = [("a", 1), ("b", 2)].iter().cloned().collect();
```

This example creates a constant `HashMap` with two entries, `("a", 1)` and `("b", 2)`. The `HashMap` is of type `HashMap<&str, i32>`, meaning it maps strings to integers.

- `const`: keyword used to declare a constant
- `MY_HASHMAP`: name of the constant
- `HashMap<&str, i32>`: type of the constant
- `[("a", 1), ("b", 2)]`: entries in the `HashMap`
- `iter()`: creates an iterator over the entries
- `cloned()`: clones the entries
- `collect()`: collects the entries into a `HashMap`

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to declare a constant Rust HashMap?](https://onelinerhub.com/rust/how-to-declare-a-constant-rust-hashmap)