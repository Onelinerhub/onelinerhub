# How do I use a variable from another file in Rust?
// plain

Variables from another file can be used in Rust by importing the file containing the variable. This can be done using the `use` keyword.

```rust
// file1.rs
pub fn foo() {
    println!("foo");
}

// file2.rs
use file1;

fn main() {
    file1::foo();
}
```

## Output example

```
foo
```

The `use` keyword imports the file containing the variable, allowing it to be used in the current file. The example above imports `file1` into `file2`, allowing the `foo` function to be called.

- `use` keyword: imports the file containing the variable
- `file1`: the file containing the variable
- `file2`: the file using the variable
- `foo`: the variable being used

## Helpful links
- [Rust Documentation - Modules](https://doc.rust-lang.org/book/ch07-02-modules-and-use-to-control-scope-and-privacy.html)

group: rust-variables