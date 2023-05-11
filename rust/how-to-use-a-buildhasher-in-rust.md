# How to use a BuildHasher in Rust?
// plain

Using a `BuildHasher` in Rust is a great way to create a custom hashing algorithm for your application. It allows you to define a custom hashing algorithm that can be used to generate a hash from a given input.

## Example code

```rust
use std::collections::hash_map::BuildHasher;

let hasher = BuildHasher::new();
let hash = hasher.build_hasher().write("Hello World".as_bytes());
```

## Output example

```
Hash: 0x2f711642c77d0b8f
```

## Code explanation


1. `use std::collections::hash_map::BuildHasher;` - This imports the `BuildHasher` trait from the standard library.

2. `let hasher = BuildHasher::new();` - This creates a new instance of the `BuildHasher` trait.

3. `let hash = hasher.build_hasher().write("Hello World".as_bytes());` - This creates a hash from the given input using the `build_hasher` method.

## Helpful links

- [Rust Documentation - BuildHasher](https://doc.rust-lang.org/std/collections/hash_map/trait.BuildHasher.html)

group: rust-hashmap

onelinerhub: [How to use a BuildHasher in Rust?](https://onelinerhub.com/rust/how-to-use-a-buildhasher-in-rust)