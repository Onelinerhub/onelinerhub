# How to use a custom hash function with a Rust HashMap?
// plain

Using a custom hash function with a Rust HashMap is easy. You can use the `HashMap::with_hasher` method to create a `HashMap` with a custom `Hasher` implementation.

```rust
use std::collections::HashMap;
use std::hash::{BuildHasher, Hasher};

struct MyHasher;

impl Hasher for MyHasher {
    fn finish(&self) -> u64 {
        0
    }

    fn write(&mut self, _bytes: &[u8]) {
        // Do nothing
    }
}

impl BuildHasher for MyHasher {
    type Hasher = MyHasher;

    fn build_hasher(&self) -> Self::Hasher {
        MyHasher
    }
}

let mut map: HashMap<&str, i32, MyHasher> = HashMap::with_hasher(MyHasher);
map.insert("foo", 42);

assert_eq!(map.get("foo"), Some(&42));
```

The code above creates a `HashMap` with a custom `Hasher` implementation called `MyHasher`. The `MyHasher` struct implements the `Hasher` and `BuildHasher` traits, and the `write` and `finish` methods. The `write` method does nothing, and the `finish` method always returns 0.

The `HashMap::with_hasher` method is then used to create a `HashMap` with the `MyHasher` hasher. The `map.insert` method is then used to insert a key-value pair into the `HashMap`. Finally, the `map.get` method is used to retrieve the value associated with the key.

## Helpful links

- [HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Hasher trait documentation](https://doc.rust-lang.org/std/hash/trait.Hasher.html)
- [BuildHasher trait documentation](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html)

group: rust-hashmap

onelinerhub: [How to use a custom hash function with a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-a-custom-hash-function-with-a-rust-hashmap)