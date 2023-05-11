# How to get the count of threads in Rust?
// plain

The `thread::spawn` function can be used to create threads in Rust. To get the count of threads, the `thread::active_count` function can be used.

```rust
use std::thread;

let thread_count = thread::active_count();
println!("Number of threads: {}", thread_count);
```

## Output example

```
Number of threads: 1
```

The code above creates a variable `thread_count` and assigns it the value returned by the `thread::active_count` function. The `println!` macro is then used to print the value of `thread_count` to the console.

## Code explanation


1. `use std::thread;` - imports the `thread` module from the `std` crate.
2. `let thread_count = thread::active_count();` - creates a variable `thread_count` and assigns it the value returned by the `thread::active_count` function.
3. `println!("Number of threads: {}", thread_count);` - prints the value of `thread_count` to the console.

## Helpful links

- [std::thread](https://doc.rust-lang.org/std/thread/index.html) - Documentation for the `std::thread` module.
- [thread::active_count](https://doc.rust-lang.org/std/thread/fn.active_count.html) - Documentation for the `thread::active_count` function.