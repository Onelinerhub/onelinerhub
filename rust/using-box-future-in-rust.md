# Using box future in Rust
// plain

Box Future is a type of Future in Rust that allows for the ownership of a value to be moved into a Future. It is a type of Future that is used to move a value from one thread to another. It is a type of Future that is used to move a value from one thread to another.

Example code:
```rust
use futures::future::BoxFuture;

fn main() {
    let future = async {
        // Do something
    };
    let boxed_future: BoxFuture<'_, ()> = Box::pin(future);
}
```

The code above creates a BoxFuture from an async block. The BoxFuture is created by using the `Box::pin` method, which takes a Future and returns a BoxFuture. The BoxFuture is then stored in the `boxed_future` variable.

The BoxFuture can then be used to move the value from one thread to another. This is done by using the `.await` method on the BoxFuture, which will block the current thread until the Future is complete.

List of ## Code explanation


- `use futures::future::BoxFuture;`: This imports the BoxFuture type from the `futures` crate.
- `let future = async { /* Do something */ };`: This creates a Future from an async block.
- `let boxed_future: BoxFuture<'_, ()> = Box::pin(future);`: This creates a BoxFuture from the Future created in the previous line. The `Box::pin` method takes a Future and returns a BoxFuture.

## Helpful links

- [Rust futures crate](https://docs.rs/futures/0.3.5/futures/)
- [BoxFuture documentation](https://docs.rs/futures/0.3.5/futures/future/struct.BoxFuture.html)

group: rust-box