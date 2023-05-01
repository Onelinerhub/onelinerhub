# How to join all futures in vector in Rust
// plain

Description: Joining all futures in a vector in Rust can be done using the `join_all` method from the `futures` crate. This method takes a vector of futures and returns a single future that resolves when all of the futures in the vector have resolved.

## Code example:
```
use futures::{future, Future};

fn join_all_futures(futures: Vec<impl Future>) -> impl Future {
    future::join_all(futures)
}
```

### Output The output of this code is a single future that resolves when all of the futures in the vector have resolved.

## Explanation of Code Parts:

- `use futures::{future, Future};`: This imports the `future` and `Future` modules from the `futures` crate.
- `fn join_all_futures(futures: Vec<impl Future>) -> impl Future {`: This defines a function called `join_all_futures` that takes a vector of futures as an argument and returns a single future.
- `future::join_all(futures)`: This calls the `join_all` method from the `futures` crate, which takes a vector of futures and returns a single future that resolves when all of the futures in the vector have resolved.

## Helpful links:

- [Futures Crate Documentation](https://docs.rs/futures/0.3.4/futures/)
- [Rust Book - Futures](https://doc.rust-lang.org/book/ch16-04-futures.html)