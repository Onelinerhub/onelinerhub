# How to write bytes to file in Rust
// plain

Writing bytes to a file in Rust is a simple process. First, you need to open a file in write-only mode using the `File::create` method. Then, you can write bytes to the file using the `write_all` method. Finally, you can close the file using the `close` method. The following ## Code example shows how to write bytes to a file in Rust:
```rust
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::create("example.txt").expect("Failed to create file");
    let bytes = b"Hello, world!";
    file.write_all(bytes).expect("Failed to write bytes");
    file.close().expect("Failed to close file");
}
```
In this example, we open a file called `example.txt` in write-only mode using the `File::create` method. Then, we write the bytes `b"Hello, world!"` to the file using the `write_all` method. Finally, we close the file using the `close` method.

## Helpful links
- [Rust Documentation - File](https://doc.rust-lang.org/std/fs/struct.File.html)
- [Rust Documentation - Write All](https://doc.rust-lang.org/std/io/trait.WriteAll.html)
- [Rust Documentation - Close](https://doc.rust-lang.org/std/fs/struct.File.html#method.close)

group: rust-files