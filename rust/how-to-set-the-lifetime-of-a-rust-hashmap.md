# How to set the lifetime of a Rust HashMap?
// plain

The lifetime of a Rust HashMap can be set by using the `HashMap::with_capacity_and_hasher` method. This method takes two parameters, the capacity and the hasher. The capacity is the maximum number of elements the HashMap can hold, and the hasher is a type that implements the `BuildHasher` trait.

## Example code

```rust
use std::collections::HashMap;
use std::hash::BuildHasher;

let mut map: HashMap<i32, i32> = HashMap::with_capacity_and_hasher(10, BuildHasher::default());
```

The code above creates a HashMap with a capacity of 10 and a default hasher.

## Code explanation


- `HashMap::with_capacity_and_hasher`: This is the method used to set the lifetime of a Rust HashMap. It takes two parameters, the capacity and the hasher.
- `capacity`: This is the maximum number of elements the HashMap can hold.
- `hasher`: This is a type that implements the `BuildHasher` trait.

List of ## Helpful links

- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to set the lifetime of a Rust HashMap?](https://onelinerhub.com/rust/how-to-set-the-lifetime-of-a-rust-hashmap)