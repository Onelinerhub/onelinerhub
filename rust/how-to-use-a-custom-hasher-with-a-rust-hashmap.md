# How to use a custom hasher with a Rust HashMap?
// plain

Using a custom hasher with a Rust HashMap is easy. You can define a custom hasher by implementing the `BuildHasher` trait. Then you can pass the hasher to the `HashMap` constructor.

```rust
use std::collections::HashMap;
use std::hash::{BuildHasher, Hasher};

struct MyHasher;

impl BuildHasher for MyHasher {
    type Hasher = MyHasher;

    fn build_hasher(&self) -> Self::Hasher {
        MyHasher
    }
}

impl Hasher for MyHasher {
    fn finish(&self) -> u64 {
        0
    }

    fn write(&mut self, _bytes: &[u8]) {
        // Do nothing
    }
}

let mut map: HashMap<&str, &str, MyHasher> = HashMap::with_hasher(MyHasher);
map.insert("foo", "bar");

assert_eq!(map.get("foo"), Some(&"bar"));
```

The code above defines a custom hasher `MyHasher` and uses it to create a `HashMap`.

1. `MyHasher` implements the `BuildHasher` trait, which provides the `build_hasher` method.
2. `MyHasher` also implements the `Hasher` trait, which provides the `finish` and `write` methods.
3. The `HashMap` constructor is called with `MyHasher` as the hasher.
4. The `insert` method is used to add a key-value pair to the `HashMap`.
5. The `get` method is used to retrieve the value associated with the key.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust BuildHasher Trait Documentation](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html)
- [Rust Hasher Trait Documentation](https://doc.rust-lang.org/std/hash/trait.Hasher.html)

group: rust-hashmap

onelinerhub: [How to use a custom hasher with a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-a-custom-hasher-with-a-rust-hashmap)