# How do I hash a string in Rust?
// plain

Hashing a string in Rust can be done using the [`hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) trait from the standard library.

## Example code

```rust
use std::hash::{Hash, Hasher};

let mut hasher = DefaultHasher::new();
"Hello World".hash(&mut hasher);
let hash = hasher.finish();
```

## Output example

```
hash = 8450045994500459945
```

The code above does the following:

1. Imports the `Hash` and `Hasher` traits from the standard library.
2. Creates a `DefaultHasher` instance.
3. Hashes the string "Hello World" using the `hash` method.
4. Stores the resulting hash in the `hash` variable.

## Helpful links

- [Hash trait documentation](https://doc.rust-lang.org/std/hash/trait.Hash.html)
- [DefaultHasher documentation](https://doc.rust-lang.org/std/hash/struct.DefaultHasher.html)