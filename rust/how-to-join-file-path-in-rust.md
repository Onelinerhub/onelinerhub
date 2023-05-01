# How to join file path in Rust
// plain

Joining file paths in Rust can be done using the `join` method from the `std::path::Path` module. This method takes two or more path components and joins them into a single path.

## Code example:
```rust
use std::path::Path;

let path1 = Path::new("/home/user/Documents");
let path2 = Path::new("example.txt");
let joined_path = path1.join(path2);
```

### Output `/home/user/Documents/example.txt`

Explanation:
- `use std::path::Path`: This imports the `Path` module from the `std::path` module.
- `let path1 = Path::new("/home/user/Documents")`: This creates a new `Path` object from the given string.
- `let path2 = Path::new("example.txt")`: This creates a new `Path` object from the given string.
- `let joined_path = path1.join(path2)`: This joins the two `Path` objects into a single path.

## Helpful links:
- [std::path::Path](https://doc.rust-lang.org/std/path/struct.Path.html)
- [Path::join](https://doc.rust-lang.org/std/path/struct.Path.html#method.join)