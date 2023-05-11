# Hashshet example in Rust
// plain

Hashset is a data structure in Rust that stores unique values. It is implemented using a hash table, which allows for fast lookups and insertion of elements.

## Example code

```rust
use std::collections::HashSet;

let mut hs = HashSet::new();

hs.insert("foo");
hs.insert("bar");

assert!(hs.contains("foo"));
```

## Output example

```
assertion successful
```

## Code explanation

- `use std::collections::HashSet;`: imports the HashSet type from the standard library
- `let mut hs = HashSet::new();`: creates a new, empty HashSet
- `hs.insert("foo");`: inserts the string "foo" into the HashSet
- `hs.insert("bar");`: inserts the string "bar" into the HashSet
- `assert!(hs.contains("foo"));`: checks if the HashSet contains the string "foo"

## Helpful links
- [Rust HashSet Documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: hashset

onelinerhub: [Hashshet example in Rust](https://onelinerhub.com/rust/hashshet-example-in-rust)