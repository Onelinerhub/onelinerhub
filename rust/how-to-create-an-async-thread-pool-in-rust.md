# How to create an async thread pool in Rust?
// plain

Creating an async thread pool in Rust is easy with the help of the `tokio` crate.

```rust
use tokio::runtime::Runtime;

let mut rt = Runtime::new().unwrap();
let pool = rt.executor();
```

This code creates a thread pool with the default number of threads.

1. `use tokio::runtime::Runtime`: imports the `Runtime` struct from the `tokio` crate.
2. `let mut rt = Runtime::new().unwrap()`: creates a new `Runtime` instance and stores it in `rt`.
3. `let pool = rt.executor()`: creates a thread pool from the `Runtime` instance and stores it in `pool`.

## Helpful links
- [Tokio Documentation](https://tokio.rs/docs/getting-started/runtime/)