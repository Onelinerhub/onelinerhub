# How to sort a Rust HashMap?
// plain

A Rust HashMap can be sorted using the `sort_by` method. This method takes a closure as an argument which is used to compare two elements of the HashMap. The closure should return `Ordering::Less` if the first element is less than the second, `Ordering::Equal` if they are equal, and `Ordering::Greater` if the first element is greater than the second.

## Example code

```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

let mut sorted_map = map.into_iter().collect::<Vec<_>>();
sorted_map.sort_by(|a, b| a.1.cmp(&b.1));
```

## Output example

```
[("a", 1), ("b", 2), ("c", 3)]
```

## Code explanation


1. `let mut map = HashMap::new();`: This creates a new empty HashMap.
2. `map.insert("a", 1);`: This inserts a key-value pair into the HashMap.
3. `let mut sorted_map = map.into_iter().collect::<Vec<_>>();`: This converts the HashMap into a vector of tuples.
4. `sorted_map.sort_by(|a, b| a.1.cmp(&b.1));`: This sorts the vector of tuples using the `sort_by` method. The closure passed to the method compares the second element of each tuple (`a.1` and `b.1`) and returns `Ordering::Less`, `Ordering::Equal`, or `Ordering::Greater` depending on the comparison result.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust sort_by method documentation](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.sort_by)

group: rust-hashmap

onelinerhub: [How to sort a Rust HashMap?](https://onelinerhub.com/rust/how-to-sort-a-rust-hashmap)