# How to use a Rust HashMap in a multithreaded environment?
// plain

Rust HashMap can be used in a multithreaded environment by using the `Arc` type. `Arc` stands for atomic reference count and is a type of pointer that allows multiple threads to access the same data. An example of using `Arc` with a HashMap is shown below:

```rust
use std::sync::Arc;
use std::collections::HashMap;

let map: HashMap<i32, i32> = HashMap::new();
let arc_map = Arc::new(map);

// Spawn threads
for i in 0..10 {
    let arc_map = arc_map.clone();
    thread::spawn(move || {
        // Access the map here
        let mut map = arc_map.lock().unwrap();
        map.insert(i, i * 2);
    });
}
```

The code above creates a HashMap and wraps it in an `Arc` type. It then spawns 10 threads which access the map and insert a key-value pair.

Parts of the code:

- `Arc::new(map)`: Creates an `Arc` type from the `map` HashMap.
- `arc_map.clone()`: Clones the `Arc` type so that each thread can access it.
- `arc_map.lock().unwrap()`: Locks the `Arc` type so that only one thread can access it at a time.
- `map.insert(i, i * 2)`: Inserts a key-value pair into the map.

## Helpful links

- [Rust Docs - Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [Rust Docs - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to use a Rust HashMap in a multithreaded environment?](https://onelinerhub.com/rust/how-to-use-a-rust-hashmap-in-a-multithreaded-environment)