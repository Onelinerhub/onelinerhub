# Zip usage example in Rust
// plain

Zip usage example in Rust:

```rust
let a = [1, 2, 3];
let b = [4, 5, 6];

let zipped = a.iter().zip(b.iter());

for (x, y) in zipped {
    println!("x = {}, y = {}", x, y);
}
```

## Output example

```
x = 1, y = 4
x = 2, y = 5
x = 3, y = 6
```

- `let a = [1, 2, 3];` creates an array of integers
- `let b = [4, 5, 6];` creates another array of integers
- `let zipped = a.iter().zip(b.iter());` creates a zipped iterator of the two arrays
- `for (x, y) in zipped {` iterates over the zipped iterator
- `println!("x = {}, y = {}", x, y);` prints the values of the two arrays

## Helpful links
- [Rust Zip Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.zip)

group: rust-zip