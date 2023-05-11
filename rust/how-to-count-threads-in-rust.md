# How to count threads in Rust?
// plain

Threads in Rust can be counted using the `thread::active_count()` function from the `std::thread` module. This function returns the number of currently active threads in the current thread's thread pool.

```rust
use std::thread;

fn main() {
    let thread_count = thread::active_count();
    println!("Number of active threads: {}", thread_count);
}
```

## Output example

```
Number of active threads: 1
```

The code above does the following:

1. Imports the `std::thread` module with `use std::thread;`
2. Calls the `thread::active_count()` function to get the number of active threads
3. Prints the number of active threads with `println!`

## Helpful links

- [std::thread](https://doc.rust-lang.org/std/thread/)