# How to abort a thread in Rust?
// plain

Threads in Rust can be aborted using the `std::thread::Thread::unpark` method. This method will cause the thread to terminate immediately.

## Example code

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from the spawned thread!");
});

handle.unpark();
```

## Output example

```
Hello from the spawned thread!
```

The code above creates a new thread using the `thread::spawn` method and then calls the `unpark` method on the thread handle to abort the thread.

## Helpful links

- [std::thread::Thread::unpark](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.unpark)