# How to use async threads in Rust?
// plain

Async threads in Rust can be used to run multiple tasks concurrently. This can be done using the `async` and `await` keywords.

## Example code

```rust
async fn hello_world() {
    println!("Hello, world!");
}

#[tokio::main]
async fn main() {
    hello_world().await;
}
```

## Output example

```
Hello, world!
```

## Code explanation

- `async fn hello_world()`: This declares an asynchronous function named `hello_world`.
- `println!("Hello, world!");`: This prints the string `Hello, world!` to the console.
- `#[tokio::main]`: This is an attribute that tells the compiler to use the Tokio runtime for the `main` function.
- `hello_world().await;`: This calls the `hello_world` function and waits for it to finish before continuing.

## Helpful links
- [Rust Async Book](https://rust-lang.github.io/async-book/)
- [Tokio Documentation](https://tokio.rs/docs/)