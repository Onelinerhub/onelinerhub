# How to lock a Rust HashMap?
// plain

A Rust HashMap can be locked using a `Mutex` or `RwLock`.

Example code using a `Mutex`:
```rust
use std::collections::HashMap;
use std::sync::Mutex;

let mut map = HashMap::new();
let mutex = Mutex::new(map);
```

The code above creates a `HashMap` and a `Mutex` to lock it.

To access the `HashMap` while it is locked, use the `lock` method of the `Mutex`:
```rust
let mut guard = mutex.lock().unwrap();
guard.insert(1, "one");
```

The code above acquires a lock on the `Mutex` and inserts a key-value pair into the `HashMap`.

## Helpful links
- [Mutex](https://doc.rust-lang.org/std/sync/struct.Mutex.html)
- [RwLock](https://doc.rust-lang.org/std/sync/struct.RwLock.html)

group: rust-hashmap

onelinerhub: [How to lock a Rust HashMap?](https://onelinerhub.com/rust/how-to-lock-a-rust-hashmap)