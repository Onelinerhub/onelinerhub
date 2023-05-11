# How to communicate between threads in Rust?
// plain

Threads in Rust can communicate through channels. Channels are a type of synchronization primitive that allows one thread to send data to another thread.

```rust
use std::sync::mpsc;

let (tx, rx) = mpsc::channel();

// Sending a message
tx.send(42).unwrap();

// Receiving a message
let received = rx.recv().unwrap();
println!("Received {}", received);
// Output: Received 42
```

1. `use std::sync::mpsc;`: imports the mpsc (multiple producer, single consumer) module from the standard library.
2. `let (tx, rx) = mpsc::channel();`: creates a new channel and returns a pair of sender (tx) and receiver (rx) endpoints.
3. `tx.send(42).unwrap();`: sends the value 42 from the sender (tx) to the receiver (rx).
4. `let received = rx.recv().unwrap();`: receives the value 42 from the receiver (rx).
5. `println!("Received {}", received);`: prints the received value.

## Helpful links

- [Rust Documentation - Channels](https://doc.rust-lang.org/std/sync/mpsc/fn.channel.html)
- [Rust by Example - Channels](https://doc.rust-lang.org/rust-by-example/std_misc/channels.html)