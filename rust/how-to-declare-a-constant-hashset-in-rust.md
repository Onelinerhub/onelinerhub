# How to declare a constant HashSet in Rust?
// plain

A constant HashSet in Rust can be declared using the `const` keyword.

```rust
const MY_HASH_SET: HashSet<i32> = [1, 2, 3].iter().cloned().collect();
```

This code creates a constant `HashSet` called `MY_HASH_SET` containing the elements `1`, `2`, and `3`. The `iter()` method creates an iterator over the array, `cloned()` creates a clone of each element, and `collect()` collects the elements into a `HashSet`.

- `const`: keyword used to declare a constant
- `MY_HASH_SET`: name of the constant
- `HashSet<i32>`: type of the constant
- `[1, 2, 3]`: array of elements to be added to the `HashSet`
- `iter()`: creates an iterator over the array
- `cloned()`: creates a clone of each element
- `collect()`: collects the elements into a `HashSet`

## Helpful links
- [Rust Documentation - Constants](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#differences-between-variables-and-constants)
- [Rust Documentation - HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: hashset

onelinerhub: [How to declare a constant HashSet in Rust?](https://onelinerhub.com/rust/how-to-declare-a-constant-hashset-in-rust)