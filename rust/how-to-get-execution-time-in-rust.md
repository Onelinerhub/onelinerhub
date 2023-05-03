# How to get execution time in Rust
// plain

Rust provides a number of ways to measure the execution time of a program.

The simplest way is to use the `std::time::Instant` type from the standard library. This type provides a `now()` method which returns an instance of `Instant` that can be used to measure the elapsed time.

## Example code

```rust
use std::time::Instant;

let start = Instant::now();

// code to measure

let elapsed = start.elapsed();
println!("Time elapsed in expensive_function() is: {:?}", elapsed);
```

## Output example

```
Time elapsed in expensive_function() is: Duration { secs: 0, nanos: 54545 }
```

## Code explanation

- `use std::time::Instant`: imports the `Instant` type from the standard library.
- `let start = Instant::now()`: creates an instance of `Instant` which will be used to measure the elapsed time.
- `let elapsed = start.elapsed()`: calculates the elapsed time since the `start` instance was created.
- `println!("Time elapsed in expensive_function() is: {:?}", elapsed)`: prints the elapsed time.

## Helpful links
- [std::time::Instant](https://doc.rust-lang.org/std/time/struct.Instant.html)

group: rust-datetime