# How to create a thread safe hashmap in Rust?
// plain

Creating a thread safe hashmap in Rust is possible using the `HashMap` type from the `std::collections` module.

```rust
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

let hashmap: Arc<Mutex<HashMap<String, String>>> = Arc::new(Mutex::new(HashMap::new()));
```

The example code above creates a thread safe `HashMap` using the `Arc` and `Mutex` types. `Arc` is used to share the `HashMap` between threads, and `Mutex` is used to ensure that only one thread can access the `HashMap` at a time.

- `Arc`: A type used to share data between threads.
- `Mutex`: A type used to ensure that only one thread can access a piece of data at a time.
- `HashMap`: A type used to store key-value pairs.

## Helpful links
- [Rust Docs - Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [Rust Docs - Mutex](https://doc.rust-lang.org/std/sync/struct.Mutex.html)
- [Rust Docs - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)