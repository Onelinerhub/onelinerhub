# How to loop async in Rust
// plain

Looping asynchronously in Rust is possible using the `async`/`await` syntax. The following example code shows how to loop asynchronously over a vector of strings:

```rust
async fn loop_async() {
    let strings = vec!["foo", "bar", "baz"];
    for s in strings {
        println!("{}", s);
    }
}
```

## Output example

```
foo
bar
baz
```

## Code explanation

- `async fn loop_async()`: declares an asynchronous function
- `let strings = vec!["foo", "bar", "baz"];`: creates a vector of strings
- `for s in strings`: loops over the vector of strings
- `println!("{}", s);`: prints the current string

## Helpful links
- [Rust async/await guide](https://rust-lang.github.io/async-book/01_getting_started/01_chapter.html)
- [Rust async/await reference](https://doc.rust-lang.org/std/keyword.async.html)

group: rust-loops