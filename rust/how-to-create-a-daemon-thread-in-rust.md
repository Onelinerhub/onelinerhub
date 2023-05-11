# How to create a daemon thread in Rust?
// plain

Creating a daemon thread in Rust is easy. All you need to do is to pass `std::thread::Builder::spawn` a `std::thread::Builder` object with `.name` and `.spawn_daemon` methods called on it.

```rust
use std::thread;

let builder = thread::Builder::new().name("daemon-thread".to_string()).spawn_daemon(|| {
    println!("I'm a daemon thread!");
});
```

## Output example

```
I'm a daemon thread!
```

## Code explanation

- `use std::thread;`: imports the `thread` module from the `std` library.
- `thread::Builder::new()`: creates a new `thread::Builder` object.
- `.name("daemon-thread".to_string())`: sets the name of the thread to `daemon-thread`.
- `.spawn_daemon(|| { ... })`: spawns a daemon thread with the given closure.

## Helpful links
- [std::thread::Builder](https://doc.rust-lang.org/std/thread/struct.Builder.html)
- [std::thread::spawn_daemon](https://doc.rust-lang.org/std/thread/fn.spawn_daemon.html)