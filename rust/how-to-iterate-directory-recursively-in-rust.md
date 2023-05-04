# How to iterate directory recursively in Rust
// plain

Iterating a directory recursively in Rust can be done using the [`WalkDir`](https://docs.rs/walkdir/2.3.1/walkdir/) crate. It provides an iterator over the entries of a directory and its subdirectories.

## Example code

```rust
use walkdir::WalkDir;

for entry in WalkDir::new("/path/to/dir") {
    let entry = entry.unwrap();
    println!("{}", entry.path().display());
}
```

## Output example

```
/path/to/dir
/path/to/dir/subdir1
/path/to/dir/subdir1/file1
/path/to/dir/subdir1/file2
/path/to/dir/subdir2
/path/to/dir/subdir2/file3
```

## Code explanation

- `use walkdir::WalkDir;`: imports the `WalkDir` crate.
- `WalkDir::new("/path/to/dir")`: creates a new `WalkDir` iterator over the entries of the directory at the given path.
- `let entry = entry.unwrap()`: unwraps the `Result` returned by the iterator.
- `println!("{}", entry.path().display())`: prints the path of the entry.

## Helpful links
- [`WalkDir` crate documentation](https://docs.rs/walkdir/2.3.1/walkdir/)

group: rust-loops