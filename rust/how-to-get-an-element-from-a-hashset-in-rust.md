# How to get an element from a HashSet in Rust?
// plain

To get an element from a HashSet in Rust, you can use the `get` method. This method takes a reference to the element you want to get and returns an `Option<&T>` where `T` is the type of the elements in the HashSet.

## Example

```rust
use std::collections::HashSet;

let mut set = HashSet::new();
set.insert(1);
set.insert(2);

let result = set.get(&1);
println!("{:?}", result);
```
## Output example

```
Some(&1)
```

The `get` method takes a reference to the element you want to get and returns an `Option<&T>` where `T` is the type of the elements in the HashSet. If the element is found, the method returns `Some(&T)`, otherwise it returns `None`.

## Helpful links
- [HashSet documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: hashset

onelinerhub: [How to get an element from a HashSet in Rust?](https://onelinerhub.com/rust/how-to-get-an-element-from-a-hashset-in-rust)