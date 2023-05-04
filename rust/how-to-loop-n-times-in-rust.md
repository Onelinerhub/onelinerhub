# How to loop N times in Rust
// plain

Looping in Rust is done using the `loop` keyword. The following example shows how to loop `N` times:

```rust
let mut n = 0;
loop {
    println!("Looping {} times", n);
    n += 1;
    if n >= N {
        break;
    }
}
```

This code will print `Looping 0 times`, `Looping 1 times`, ..., `Looping N-1 times`.

The code consists of the following parts:

1. `let mut n = 0;`: This declares a mutable variable `n` and initializes it to `0`.
2. `loop {`: This starts the loop.
3. `println!("Looping {} times", n);`: This prints the current loop count.
4. `n += 1;`: This increments the loop count.
5. `if n >= N {`: This checks if the loop count is greater than or equal to `N`.
6. `break;`: This exits the loop if the condition is true.
7. `}`: This closes the loop.

## Helpful links

- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-loops