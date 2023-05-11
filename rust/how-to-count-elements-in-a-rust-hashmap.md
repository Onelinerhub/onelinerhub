# How to count elements in a Rust HashMap?
// plain

To count elements in a Rust HashMap, you can use the `len()` method. This method returns the number of elements in the HashMap.

## Example code

```
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);

println!("Number of elements in the map: {}", map.len());
```

## Output example

```
Number of elements in the map: 2
```

## Code explanation


1. `use std::collections::HashMap;`: This line imports the `HashMap` type from the `std::collections` module.

2. `let mut map = HashMap::new();`: This line creates a new empty `HashMap` and stores it in the `map` variable.

3. `map.insert("a", 1);` and `map.insert("b", 2);`: These lines insert two key-value pairs into the `map` HashMap.

4. `println!("Number of elements in the map: {}", map.len());`: This line prints the number of elements in the `map` HashMap.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to count elements in a Rust HashMap?](https://onelinerhub.com/rust/how-to-count-elements-in-a-rust-hashmap)