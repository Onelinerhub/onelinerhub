# How to iterate through hashmap values in Rust
// plain

Iterating through the values of a HashMap in Rust can be done using the `values()` method. This returns an iterator over the values of the HashMap. The following example code block shows how to iterate through the values of a HashMap:

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

for value in map.values() {
    println!("{}", value);
}
```

## Output example

```
1
2
3
```

## Code explanation


1. `use std::collections::HashMap`: This imports the `HashMap` type from the `std::collections` module.
2. `let mut map = HashMap::new()`: This creates a new empty `HashMap` and stores it in the `map` variable.
3. `map.insert("a", 1)`: This inserts a key-value pair into the `map` HashMap.
4. `for value in map.values()`: This starts an iterator over the values of the `map` HashMap.
5. `println!("{}", value)`: This prints the current value of the iterator.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-loops