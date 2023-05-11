# How to compare two HashSets in Rust?
// plain

Comparing two HashSets in Rust is easy and efficient. The `HashSet::is_subset` and `HashSet::is_superset` methods can be used to compare two HashSets.

## Example code

```rust
let set_a: HashSet<i32> = [1, 2, 3].iter().cloned().collect();
let set_b: HashSet<i32> = [2, 3, 4].iter().cloned().collect();

assert!(set_a.is_subset(&set_b));
assert!(!set_b.is_subset(&set_a));
```

## Output example

```
assertion successful
assertion successful
```

## Code explanation


1. `let set_a: HashSet<i32> = [1, 2, 3].iter().cloned().collect();` - This line creates a `HashSet` called `set_a` with elements `1`, `2`, and `3`.
2. `let set_b: HashSet<i32> = [2, 3, 4].iter().cloned().collect();` - This line creates a `HashSet` called `set_b` with elements `2`, `3`, and `4`.
3. `assert!(set_a.is_subset(&set_b));` - This line checks if `set_a` is a subset of `set_b`.
4. `assert!(!set_b.is_subset(&set_a));` - This line checks if `set_b` is not a subset of `set_a`.

## Helpful links

- [HashSet documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: hashset

onelinerhub: [How to compare two HashSets in Rust?](https://onelinerhub.com/rust/how-to-compare-two-hashsets-in-rust)