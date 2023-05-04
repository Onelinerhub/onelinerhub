# How to iterate directory in Rust
// plain

Iterating through a directory in Rust can be done using the `std::fs::read_dir` function. This function takes a path as an argument and returns an iterator of `std::fs::DirEntry` objects.

## Example code

```rust
use std::fs;

fn main() {
    let dir = "./";
    for entry in fs::read_dir(dir).unwrap() {
        let entry = entry.unwrap();
        println!("{:?}", entry.path());
    }
}
```

## Output example

```
"./src"
"./Cargo.lock"
"./Cargo.toml"
"./target"
```

## Code explanation

- `use std::fs;`: imports the `fs` module from the `std` library.
- `let dir = "./";`: sets the directory to iterate over.
- `fs::read_dir(dir).unwrap()`: calls the `read_dir` function with the `dir` argument and unwraps the result.
- `let entry = entry.unwrap();`: unwraps the `entry` object.
- `println!("{:?}", entry.path());`: prints the path of the `entry` object.

## Helpful links
- [std::fs::read_dir](https://doc.rust-lang.org/std/fs/fn.read_dir.html)

group: rust-loops