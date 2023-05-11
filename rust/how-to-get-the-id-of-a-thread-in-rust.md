# How to get the ID of a thread in Rust?
// plain

The ID of a thread in Rust can be obtained using the `thread::current().id()` method. This method returns a `ThreadId` struct which contains the ID of the current thread.

## Example code

```rust
use std::thread;

let thread_id = thread::current().id();
println!("Thread ID: {:?}", thread_id);
```

## Output example

```
Thread ID: ThreadId { inner: 0x7f8f9f8f8f8f8f8f }
```

## Code explanation

- `thread::current()`: This method returns a `Thread` struct which contains information about the current thread.
- `.id()`: This method is used to get the ID of the current thread. It returns a `ThreadId` struct.
- `println!`: This macro is used to print the thread ID to the console.

## Helpful links
- [Threads in Rust](https://doc.rust-lang.org/book/ch16-02-threads.html)
- [Thread::current()](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.current)
- [ThreadId](https://doc.rust-lang.org/std/thread/struct.ThreadId.html)