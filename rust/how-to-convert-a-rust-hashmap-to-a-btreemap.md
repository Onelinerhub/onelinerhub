# How to convert a Rust HashMap to a BTreeMap?
// plain

To convert a Rust `HashMap` to a `BTreeMap`, you can use the `.into_iter()` method to iterate over the `HashMap` and the `.collect()` method to collect the elements into a `BTreeMap`.

## Example code

```rust
let mut hashmap = HashMap::new();
hashmap.insert("a", 1);
hashmap.insert("b", 2);

let btreemap: BTreeMap<_, _> = hashmap.into_iter().collect();
```

## Output example

```
btreemap = {"a": 1, "b": 2}
```

## Code explanation


1. `let mut hashmap = HashMap::new();`: This line creates a new empty `HashMap` called `hashmap`.
2. `hashmap.insert("a", 1);`: This line inserts a key-value pair `("a", 1)` into the `HashMap`.
3. `hashmap.insert("b", 2);`: This line inserts a key-value pair `("b", 2)` into the `HashMap`.
4. `let btreemap: BTreeMap<_, _> = hashmap.into_iter().collect();`: This line uses the `.into_iter()` method to iterate over the `HashMap` and the `.collect()` method to collect the elements into a `BTreeMap`.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust BTreeMap documentation](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html)

group: rust-hashmap

onelinerhub: [How to convert a Rust HashMap to a BTreeMap?](https://onelinerhub.com/rust/how-to-convert-a-rust-hashmap-to-a-btreemap)