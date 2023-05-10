# How do I use a variable number of arguments in Rust?
// plain

Rust supports variable number of arguments using the `std::env::args()` function. This function returns an iterator over the arguments passed to the program.

```rust
fn main() {
    let args: Vec<String> = std::env::args().collect();
    println!("{:?}", args);
}
```

## Output example

```
["/usr/local/bin/rustrun", "my_program.rs", "arg1", "arg2"]
```

The code above collects the arguments passed to the program into a vector of strings.

1. `std::env::args()`: This function returns an iterator over the arguments passed to the program.
2. `collect()`: This method collects the iterator into a vector of strings.

## Helpful links

- [std::env::args()](https://doc.rust-lang.org/std/env/fn.args.html)
- [collect()](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-variables