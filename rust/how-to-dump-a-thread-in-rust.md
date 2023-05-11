# How to dump a thread in Rust?
// plain

Dumping a thread in Rust is done using the `thread::park()` function. This function will block the current thread until it is unparked.

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});

handle.thread().unpark();
thread::park();
```

The code above will spawn a new thread and then unpark it. The main thread will then be parked until the spawned thread is finished.

- `thread::spawn()`: spawns a new thread
- `handle.thread().unpark()`: unpark the spawned thread
- `thread::park()`: park the main thread

## Helpful links

- [std::thread::park()](https://doc.rust-lang.org/std/thread/fn.park.html)
- [std::thread::spawn()](https://doc.rust-lang.org/std/thread/fn.spawn.html)