# How to loop await in Rust
// plain

Looping `await` in Rust is done using a `loop` statement. The `await` keyword is used to wait for a `Future` to complete before continuing the loop.

## Example code

```rust
loop {
    let result = await!(future);
    // Do something with result
}
```

## Output example

```
None
```

## Code explanation

- `loop`: This statement is used to create a loop that will execute until it is broken out of.
- `await!`: This macro is used to wait for a `Future` to complete before continuing the loop.
- `future`: This is a `Future` that will be awaited on.

## Helpful links
- [Rust `loop` Statement](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [`await!` Macro](https://docs.rs/futures/0.1.25/futures/macro.await.html)

group: rust-loops