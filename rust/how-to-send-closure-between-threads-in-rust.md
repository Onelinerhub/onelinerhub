# How to send closure between threads in Rust
// plain

In Rust, closures can be sent between threads using the `std::thread::spawn` function. This function takes a closure as an argument and spawns a new thread to execute the closure. The closure can be used to communicate data between threads, such as sending a result from one thread to another. To ensure thread safety, the closure should be wrapped in a `Mutex` or `RwLock` to prevent data races. Additionally, the `std::sync::mpsc` module can be used to send messages between threads. This module provides a channel-based communication system, allowing threads to send messages to each other.

```rust
use std::thread;
use std::sync::{Mutex, Arc};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data_clone = data.clone();

let handle = thread::spawn(move || {
    let mut data = data_clone.lock().unwrap();
    data.push(4);
});

handle.join().unwrap();

let data = data.lock().unwrap();
assert_eq!(*data, vec![1, 2, 3, 4]);
```

In the example above, a closure is sent to a new thread using the `std::thread::spawn` function. The closure is wrapped in a `Mutex` to ensure thread safety. The closure is then used to modify the data in the `data` variable, which is shared between the two threads.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Threads](https://doc.rust-lang.org/book/ch16-00-concurrency.html)
- [Rust Mutex](https://doc.rust-lang.org/std/sync/struct.Mutex.html)

group: rust-closure