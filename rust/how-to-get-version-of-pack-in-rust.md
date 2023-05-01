# How to get version of pack in Rust
// plain

You can get the version of a pack in Rust using the `version()` method. This method is part of the `Cargo.toml` manifest file, which is used to define the dependencies and other metadata of a Rust project.

Below is an example of how to use the `version()` method to get the version of a pack:

```rust
fn main() {
    let version = Cargo.toml.version();
    println!("Version of pack is: {}", version);
}
```

### Output

Version of pack is: 0.1.0

Explanation:

- `fn main()`: This is the main function of the program, which is the entry point for the program.
- `let version = Cargo.toml.version()`: This line uses the `version()` method to get the version of the pack from the `Cargo.toml` manifest file.
- `println!("Version of pack is: {}", version)`: This line prints the version of the pack to the console.

## Helpful links:

- [Cargo.toml Manifest File](https://doc.rust-lang.org/cargo/reference/manifest.html)
- [Rust Programming Language](https://www.rust-lang.org/)