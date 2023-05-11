# How to create a HashSet from a Vec in Rust?
// plain

Creating a HashSet from a Vec in Rust is easy and can be done with the `collect` method.

```rust
let vec = vec![1, 2, 3];
let set: HashSet<i32> = vec.into_iter().collect();
```

The output of the above code will be a `HashSet` containing the elements of the `Vec`:
```
{1, 2, 3}
```

The code works by taking the elements of the `Vec` and collecting them into a `HashSet`. The `collect` method takes an iterator and collects its elements into a collection.

## Helpful links
- [Rust Docs - Collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: hashset

onelinerhub: [How to create a HashSet from a Vec in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashset-from-a-vec-in-rust)