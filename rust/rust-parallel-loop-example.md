# Rust parallel loop example
// plain

Parallel loops in Rust are implemented using the Rayon library. Rayon provides a `par_iter` method which can be used to iterate over a collection in parallel.

```rust
use rayon::prelude::*;

let v = vec![1, 2, 3];

// Iterate over `v` in parallel
v.par_iter().for_each(|x| println!("{}", x));
```

## Output example

```
1
2
3
```

The code above uses the `par_iter` method to iterate over the vector `v` in parallel. The `for_each` method is then used to execute a closure for each element in the vector.

## Helpful links
- [Rayon Documentation](https://docs.rs/rayon/1.3.0/rayon/)

group: rust-loops